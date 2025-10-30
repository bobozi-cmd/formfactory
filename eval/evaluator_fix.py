import asyncio
from difflib import SequenceMatcher
import os
import json
import argparse
from pathlib import Path
import time
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from agentrr.model.openai_server import OpenAIServer
from agentrr.plugins.index_wrapper import IndexWrapper
from agentrr.replayer.codegen_replayer import CodegenReplayer
from agentrr.replayer.codegen_planner import CodegenPlanner
from agentrr.expdb.loader import collect_tasks_spec

os.environ["TRANSFORMERS_VERBOSITY"] = "error"

GROUND_TRUTH_DIR = Path('../data/data1')
TASK_DIR = Path('../data/data2')

TASKS_MAPPING = {
    "A11": ("job_applications.txt", "/academic-research/job-application", "job_applications.json"),
    "A12": ("grant_applications.txt", "/academic-research/grant-application", "grant_applications.json"),
    "A15": ("student_courses.txt", "/academic-research/course-registration", "student_courses.json"),
    "A14": ("paper_submissions.txt", "/academic-research/paper-submission", "paper_submissions.json"),
    "A13": ("scholarship_applications.txt", "/academic-research/scholarship-application", "scholarship_applications.json"),
    "B11": ("startup_funding_applications.txt", "/professional-business/startup-funding", "startup_funding_applications.json"),
    "B12": ("real_estate_rental_applications.txt", "/professional-business/rental-application", "real_estate_rental_applications.json"),
    "B13": ("workshop_registrations.txt", "/professional-business/workshop-registration", "workshop_registrations.json"),
}

FUZZY_FIELD = {
    "A11": ["cover_letter", 'department'],
    "A12": [],
    "A15": ["comments"],
    "A14": ["abstract"],
    "A13": ["essay"], # TODO
}

api_key = os.getenv("OPENAI_API_KEY", None)
base_url = os.getenv("OPENAI_BASE_URL", None)
model = os.getenv("LLM_MODEL", "gpt-4o")
# --------------------------------------------------------


class TaskExtractor:
    def __init__(self, task_file: Path):
        self.file = task_file
        self.tasks = []

        self._split()
    
    def _split(self):
        idx = 1
        
        task_line = []
        with open(self.file, 'r') as fp:
            for line in fp.readlines():
                if line.startswith(str(idx)):
                    if task_line != []:
                        self.tasks.append("".join(task_line))
                    if line.startswith(f'{idx}.'):
                        task_line = [line.removeprefix(f'{idx}.')]
                    elif line.startswith(f'{idx})'):
                        task_line = [line.removeprefix(f'{idx})')]
                    else:
                        assert False, f"Cannot remove prefix: {line[:100]}"
                    idx += 1
                else:
                    task_line.append(line)
        
        if task_line != []:
            self.tasks.append("".join(task_line))

        print(f"Extract {len(self.tasks)} tasks")

    def get_task(self, idx):
        return self.tasks[idx]


class FormFieldEvaluator:
    def __init__(self, task, ground_truth_file: Path, eval_file: Path, evaluation_output_file: Path, sbert_name = 'all-MiniLM-L6-v2', word_sbert_name = 'all-mpnet-base-v2'):
        self.task = task
        self.ground_truth_file = ground_truth_file
        self.eval_file = eval_file
        self.evaluation_output_file = evaluation_output_file
        self.sbert = SentenceTransformer(sbert_name)
        self.word_sbert = SentenceTransformer(word_sbert_name)

    def evaluate(self):
        gt_data = load_json(self.ground_truth_file)
        predict_data = load_json(self.eval_file)
        
        print(f"All data: {len(predict_data)}")
        
        durs = []
        scores = []
        all_score = 0
        for predict_item in predict_data:
            gt_item = gt_data[predict_item['task']]
            match_data = self._evaluate_item(predict_item['result'], gt_item)
            
            durs.append(predict_item['dur'])
            scores.append(match_data['got_score']/match_data['all_score'])
            all_score += match_data['all_score']
            print(f"🫡 [{predict_item['task']}] score: {match_data['got_score']} / {match_data['all_score']} = {scores[-1]:.3f}")

        duration_data = self.analysis(durs, 'dur')
        score_data = self.analysis(scores, 'score')

        ret = {
            "task": self.task,
            "dur": duration_data,
            "score": score_data
        }

        return ret

    def calculate_text_similarity(self, text1: str, text2: str, word_level = False) -> float:
        """Calculate similarity between two text strings."""
        if not text1 or not text2:
            return 0.0
        text1 = text1.strip().lower()
        text2 = text2.strip().lower()
        if text1 == text2:
            return 1.0

        if word_level:
            embeddings = self.word_sbert.encode([text1, text2], show_progress_bar=False)
        else:
            embeddings = self.sbert.encode([text1, text2], show_progress_bar=False)

        similarity = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]
        
        return float(similarity)

    def _evaluate_item(self, predict: dict, ground_truth: dict):
        """Evaluate a single item against ground truth."""
        got_score = 0
        all_score = 0
        for field, val in ground_truth.items():
            if isinstance(val, str):
                if field in FUZZY_FIELD[self.task]:
                    if len(predict[field]) < 50:
                        similarity = self.calculate_text_similarity(val, predict[field], word_level=True)
                    else:
                        similarity = self.calculate_text_similarity(val, predict[field])

                    if similarity > 0.5:
                        got_score += 1
                    else:
                        print(field, "got low similarity: ", similarity)
                    all_score += 1
                else:
                    if field in predict and predict[field] == val:
                        got_score += 1
                    all_score += 1
            elif isinstance(val, int):
                if field in predict and predict[field] == val:
                    got_score += 1
                all_score += 1
            elif isinstance(val, float):
                if field in predict and abs(predict[field] - val) < 0.001:
                    got_score += 1
                all_score += 1
            elif isinstance(val, list):
                if field in predict:
                    for v in val:
                        if v in predict[field]:
                            got_score += 1
                all_score += len(val)
            else:
                print(f"Cannot handle {field}:{val} ({type(val)})")
        
        ret = {
            "got_score": got_score,
            "all_score": all_score,
        }

        return ret

    def analysis(self, datas: list, name: str):
        ret = {}
        
        ret["mean_"] = np.mean(datas)
        ret["median_"] = np.median(datas)
        ret["p99_"] = np.percentile(datas, 99)
        ret["p95_"] = np.percentile(datas, 95)
        ret["p90_"] = np.percentile(datas, 90)
        ret["p75_"] = np.percentile(datas, 75)
        ret["p50_"] = np.percentile(datas, 50)
        ret["p25_"] = np.percentile(datas, 25)

        ret["std_"] = np.std(datas)
        ret["var_"] = np.var(datas)
        ret["min_"] = np.min(datas)
        ret["max_"] = np.max(datas)

        print("=" * 10, f"[{name}]", "=" * 10)
        print(f"平均值: {ret['mean_']:.2f}")
        print(f"中位数: {ret['median_']:.2f}")
        print(f"P99: {ret['p99_']:.2f}")
        print(f"P95: {ret['p95_']:.2f}")
        print(f"标准差: {ret['std_']:.2f}")

        return ret


class AgentRR:
    def __init__(self, exp_db, url):
        self.url = url
        self.spec = collect_tasks_spec(exp_db)[url]
        self.llm = OpenAIServer(model, api_key=api_key, base_url=base_url)

    async def execute_task(self, task, max_step: int = 10):
        task += f"\n如果输入任务是英文, 你的所有输出都要是英文.\n"
        planner = CodegenPlanner(self.spec, task)
        replayer = CodegenReplayer()

        result = await planner.decompose_task(self.llm)

        if result is False:
            print("❌ Planning error")
        else:
            await replayer.setup(self.url)
            await asyncio.sleep(1)

            last_snapshot = None

            step = 0

            while step < max_step:
                step += 1
                snapshot = await IndexWrapper.fast_screenshot(replayer.context)
                plan = await planner.next(snapshot, last_snapshot, self.llm)
                print(f"🤔: {plan.think}")

                if plan.func in planner.a11y:
                    success_call = False
                    for level in planner.a11y[plan.func]:
                        try:
                            if level == 'low':
                                await replayer.low_level_replay(planner.func[plan.func], plan.arguments)
                            success_call = True
                        except Exception as e:
                            print(f"❌ {level}-level replay failed: {e}")
                    
                        if success_call:
                            break
                
                    if not success_call:
                        print(f"❌ Failed to execute subtask: {plan.think}")
                        break
            
                if plan.done:
                    if planner.next_stage():
                        print(f"✅ Finished task")
                        break
                    continue

            await replayer.close()
        

def remove_file(file: Path):
    if file.exists():
        os.remove(file)

def load_json(file: Path):
    with open(file, 'r') as fp:
        return json.load(fp)

def dump_json(file: Path, data):
    with open(file, 'w') as fp:
        json.dump(data, fp, indent=4)


async def main(args):
    start = args.start
    end = args.end

    task_file = TASK_DIR / TASKS_MAPPING[args.task][0]
    url = f"{args.base_url}{TASKS_MAPPING[args.task][1]}"
    submission_file: Path = args.submission / f"{args.task}.json"
    out_file: Path = Path(f"./tmp_{args.task}_out_{start}_{end}.json")
    exp_db_dir: Path = args.dir

    
    print(f"📍 task_file: {task_file.absolute()}")
    print(f"👉 {url = }")
    print(f"📁 submission_file: {submission_file.absolute()}")
    print(f"📁 out_file: {out_file.absolute()}")
    print(f"📁 exp_db_dir: {exp_db_dir.absolute()}")

    # clear legacy submission file
    remove_file(submission_file)

    task_extractor = TaskExtractor(task_file)
    agent = AgentRR(exp_db=exp_db_dir, url=url)
    
    results = []

    for i in range(len(task_extractor.tasks))[start:end]:
        data = {"task": i}
        
        task = task_extractor.get_task(i)
        # q = input("> ")
        # if q.lower() == 'q':
        #     break

        t1 = time.time()
        try:
            await agent.execute_task(task)
        except Exception as e:
            print(f"❌ execute failed: {e}")

        t2 = time.time()
        run_time = t2 - t1
        data['dur'] = run_time
        print(f"⏱️ [{i}] Task execute in {run_time:.2f} s")

        if submission_file.exists():
            try:
                data['result'] = load_json(submission_file)[0]
            except Exception as e:
                data['result'] = {}
            finally:
                remove_file(submission_file)
        else:
            data['result'] = {}

        results.append(data)
        # 实时更新
        dump_json(out_file, results)


def eval(args):
    assert args.eval_file, "For eval, must provide eval file by --eval-file"
    eval_file: Path = args.eval_file
    gt_file = GROUND_TRUTH_DIR / TASKS_MAPPING[args.task][2]
    out_file = Path(f"./{args.task}_eval_result.json")

    print(f"📍 gt_file: {gt_file.absolute()}")
    print(f"📍 eval_file: {eval_file.absolute()}")
    print(f"📍 out_file: {out_file.absolute()}")

    evaluator = FormFieldEvaluator(args.task, gt_file, eval_file, out_file)
    ret = evaluator.evaluate()
    dump_json(out_file, ret)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", required=True, type=str, choices=list(TASKS_MAPPING.keys()))
    parser.add_argument("-d", "--dir", help="exp_db", type=Path, required=True)
    parser.add_argument('-e', '--eval', action='store_true')
    parser.add_argument('--eval-file', type=Path)
    parser.add_argument("-u", "--base-url", default="http://127.0.0.1:5000", type=str)
    parser.add_argument("--submission", type=Path, default="../submission")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=50)

    args = parser.parse_args()

    if args.eval:
        eval(args)
    else:
        asyncio.run(main(args))
