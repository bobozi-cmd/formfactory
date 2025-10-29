import asyncio
import os
import json
import argparse
from pathlib import Path
import time
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import re

from agentrr.model.openai_server import OpenAIServer
from agentrr.plugins.index_wrapper import IndexWrapper
from agentrr.replayer.codegen_replayer import CodegenReplayer
from agentrr.replayer.codegen_planner import CodegenPlanner
from agentrr.expdb.loader import collect_tasks_spec

GROUND_TRUTH_DIR = Path('../data/data1')
TASK_DIR = Path('../data/data2')

TASKS_MAPPING = {
    "A11": ("job_applications.txt", "/academic-research/job-application", "job_applications.json"),
    "A12": ("grant_applications.txt", "/academic-research/grant-application", "grant_applications.json"),
    "A15": ("student_courses.txt", "/academic-research/course-registration", "student_courses.json"),
    "A14": ("paper_submissions.txt", "/academic-research/paper-submission", "paper_submissions.json"),
    "A13": ("scholarship_applications.txt", "/academic-research/scholarship-application", "scholarship_applications.json"),
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
    def __init__(self, 
                 ground_truth_dir: str = "../data/data1",
                 results_dir: str = "../submission",
                 evaluation_output_dir: str = "evaluation_results"):
        """
        Initialize the evaluator.
        
        Args:
            ground_truth_dir (str): Directory containing ground truth JSON files
            results_dir (str): Directory containing model prediction results
            evaluation_output_dir (str): Directory to save evaluation results
        """
        self.ground_truth_dir = Path(ground_truth_dir)
        self.results_dir = Path(results_dir)
        self.evaluation_output_dir = Path(evaluation_output_dir)
        
        # Create evaluation output directory
        self.evaluation_output_dir.mkdir(exist_ok=True)

    def evaluate_single_file(self, ground_truth_filename: str, result_file: str) -> Dict[str, Any]:
        """Evaluate a single prediction file against ground truth."""


class AgentRR:
    def __init__(self, exp_db, url):
        self.url = url
        self.spec = collect_tasks_spec(exp_db)[url]
        self.llm = OpenAIServer(model, api_key=api_key, base_url=base_url)

    async def execute_task(self, task):
        planner = CodegenPlanner(self.spec, task)
        replayer = CodegenReplayer()

        result = await planner.decompose_task(self.llm)

        if result is False:
            print("❌ Planning error")
        else:
            await replayer.setup(self.url)
            await asyncio.sleep(1)

            last_snapshot = None

            while True:
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
    task_file = TASK_DIR / TASKS_MAPPING[args.task][0]
    gt_file = GROUND_TRUTH_DIR / TASKS_MAPPING[args.task][2]
    url = f"{args.base_url}{TASKS_MAPPING[args.task][1]}"
    submission_file: Path = args.submission / f"{args.task}.json"
    out_file: Path = Path(f"./tmp_{args.task}_out.json")
    exp_db_dir: Path = args.dir
    
    print(f"📍 task_file: {task_file.absolute()}")
    print(f"📍 gt_file: {gt_file.absolute()}")
    print(f"👉 {url = }")
    print(f"📁 submission_file: {submission_file.absolute()}")
    print(f"📁 out_file: {out_file.absolute()}")
    print(f"📁 exp_db_dir: {exp_db_dir.absolute()}")

    # clear legacy submission file
    remove_file(submission_file)

    task_extractor = TaskExtractor(task_file)
    agent = AgentRR(exp_db=exp_db_dir, url=url)
    
    results = []

    for i in range(len(task_extractor.tasks)):
        data = {"task": i}
        
        task = task_extractor.get_task(i)
        q = input("> ")
        if q.lower() == 'q':
            break

        t1 = time.time()
        try:
            await agent.execute_task(task)
        except Exception as e:
            pass
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

    dump_json(out_file, results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", required=True, type=str, choices=list(TASKS_MAPPING.keys()))
    parser.add_argument("-u", "--base-url", default="http://127.0.0.1:5000", type=str)
    parser.add_argument("-d", "--dir", help="exp_db", type=Path, required=True)
    parser.add_argument("--submission", type=Path, default="../submission")

    args = parser.parse_args()

    asyncio.run(main(args))
