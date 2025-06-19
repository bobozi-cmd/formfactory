import os
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import re
from difflib import SequenceMatcher

class FormFieldEvaluator:
    def __init__(self, 
                 ground_truth_dir: str = "../data/data1",
                 results_dir: str = "output",
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
        
        # Common field mappings for form analysis
        self.field_mappings = {
            "name": ["name", "artist name", "applicant name", "full name", "author name"],
            "email": ["email", "email address", "contact email", "e-mail"],
            "title": ["title", "artwork title", "project title", "submission title"],
            "description": ["description", "artwork description", "project description", "summary"],
            "medium": ["medium", "art medium", "material", "technique"],
            "dimensions": ["dimensions", "size", "measurements"],
            "year": ["year", "year created", "creation year", "date"],
            "price": ["price", "cost", "fee", "amount"],
            "available": ["available", "for sale", "availability"]
        }

    def load_ground_truth(self, filename: str) -> Optional[List[Dict[str, Any]]]:
        """Load ground truth data from JSON file."""
        try:
            file_path = self.ground_truth_dir / f"{filename}.json"
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else [data]
        except Exception as e:
            print(f"Error loading ground truth {filename}: {e}")
            return None

    def load_prediction_results(self, result_file: str) -> Optional[Dict[str, Any]]:
        """Load model prediction results from JSON file."""
        try:
            file_path = self.results_dir / result_file
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading prediction results {result_file}: {e}")
            return None

    def extract_fields_from_prediction(self, prediction_text: str) -> Dict[str, str]:
        """Extract structured fields from model prediction text."""
        extracted_fields = {}
        
        # Common patterns for field extraction
        patterns = {
            "name": [
                r"(?:name|artist|applicant):\s*([^\n]+)",
                r"(?:name|artist|applicant)\s*is\s*([^\n,.]+)",
                r"([A-Z][a-z]+ [A-Z][a-z]+)",  # Name pattern
            ],
            "email": [
                r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",
                r"email:\s*([^\s\n]+)",
            ],
            "title": [
                r"(?:title|titled|artwork):\s*[\"']?([^\"'\n]+)[\"']?",
                r"(?:title|titled|artwork)\s*[\"']([^\"']+)[\"']",
            ],
            "medium": [
                r"medium:\s*([^\n]+)",
                r"(?:medium|technique|material):\s*([^\n]+)",
            ],
            "dimensions": [
                r"dimensions?:\s*([^\n]+)",
                r"(\d+\s*x\s*\d+(?:\s*x\s*\d+)?(?:\s*cm)?)",
            ],
            "year": [
                r"(?:year|created|made):\s*(\d{4})",
                r"(?:in|from)\s*(\d{4})",
            ]
        }
        
        for field, field_patterns in patterns.items():
            for pattern in field_patterns:
                matches = re.findall(pattern, prediction_text, re.IGNORECASE)
                if matches:
                    extracted_fields[field] = matches[0].strip()
                    break
        
        return extracted_fields

    def normalize_field_name(self, field_name: str) -> str:
        """Normalize field names for comparison."""
        field_lower = field_name.lower().strip()
        
        for standard_field, variations in self.field_mappings.items():
            if field_lower in variations:
                return standard_field
        
        return field_lower

    def calculate_text_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two text strings."""
        if not text1 or not text2:
            return 0.0
        
        # Normalize texts
        text1_norm = re.sub(r'\s+', ' ', str(text1).lower().strip())
        text2_norm = re.sub(r'\s+', ' ', str(text2).lower().strip())
        
        # Calculate similarity using SequenceMatcher
        similarity = SequenceMatcher(None, text1_norm, text2_norm).ratio()
        return similarity

    def evaluate_field_extraction(self, 
                                ground_truth: List[Dict[str, Any]], 
                                predictions: Dict[str, str]) -> Dict[str, Any]:
        """Evaluate field extraction accuracy."""
        
        # Flatten ground truth data
        all_gt_fields = {}
        for item in ground_truth:
            for key, value in item.items():
                normalized_key = self.normalize_field_name(key)
                if normalized_key not in all_gt_fields:
                    all_gt_fields[normalized_key] = []
                all_gt_fields[normalized_key].append(str(value))
        
        # Normalize prediction field names
        normalized_predictions = {}
        for key, value in predictions.items():
            normalized_key = self.normalize_field_name(key)
            normalized_predictions[normalized_key] = str(value)
        
        # Calculate metrics
        field_scores = {}
        total_precision = 0
        total_recall = 0
        total_f1 = 0
        matched_fields = 0
        
        # Evaluate each ground truth field
        for gt_field, gt_values in all_gt_fields.items():
            if gt_field in normalized_predictions:
                pred_value = normalized_predictions[gt_field]
                
                # Find best matching ground truth value
                best_similarity = 0
                for gt_value in gt_values:
                    similarity = self.calculate_text_similarity(pred_value, gt_value)
                    best_similarity = max(best_similarity, similarity)
                
                field_scores[gt_field] = {
                    "predicted": pred_value,
                    "ground_truth": gt_values,
                    "similarity": best_similarity,
                    "found": True
                }
                
                total_precision += best_similarity
                total_recall += best_similarity
                matched_fields += 1
            else:
                field_scores[gt_field] = {
                    "predicted": None,
                    "ground_truth": gt_values,
                    "similarity": 0.0,
                    "found": False
                }
        
        # Calculate overall metrics
        num_gt_fields = len(all_gt_fields)
        num_pred_fields = len(normalized_predictions)
        
        precision = (total_precision / num_pred_fields) if num_pred_fields > 0 else 0
        recall = (total_recall / num_gt_fields) if num_gt_fields > 0 else 0
        f1_score = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0
        
        return {
            "field_scores": field_scores,
            "overall_metrics": {
                "precision": precision,
                "recall": recall,
                "f1_score": f1_score,
                "fields_found": matched_fields,
                "total_gt_fields": num_gt_fields,
                "total_pred_fields": num_pred_fields
            }
        }

    def evaluate_content_accuracy(self, 
                                ground_truth: List[Dict[str, Any]], 
                                prediction_text: str) -> Dict[str, Any]:
        """Evaluate content accuracy based on information coverage."""
        
        # Extract all text content from ground truth
        gt_text_content = []
        for item in ground_truth:
            for key, value in item.items():
                if isinstance(value, str) and len(value) > 10:  # Substantial text content
                    gt_text_content.append(value.lower())
        
        prediction_lower = prediction_text.lower()
        
        # Calculate coverage metrics
        covered_content = 0
        total_content = len(gt_text_content)
        content_similarities = []
        
        for gt_content in gt_text_content:
            # Check if content is mentioned or similar content exists
            similarity = self.calculate_text_similarity(gt_content, prediction_lower)
            content_similarities.append(similarity)
            
            if similarity > 0.3:  # Threshold for considering content as covered
                covered_content += 1
        
        coverage_ratio = covered_content / total_content if total_content > 0 else 0
        avg_similarity = sum(content_similarities) / len(content_similarities) if content_similarities else 0
        
        return {
            "coverage_ratio": coverage_ratio,
            "average_similarity": avg_similarity,
            "covered_items": covered_content,
            "total_items": total_content,
            "content_similarities": content_similarities
        }

    def evaluate_single_file(self, ground_truth_filename: str, result_file: str) -> Dict[str, Any]:
        """Evaluate a single prediction file against ground truth."""
        
        print(f"Evaluating {result_file} against {ground_truth_filename}")
        
        # Load data
        ground_truth = self.load_ground_truth(ground_truth_filename)
        prediction_result = self.load_prediction_results(result_file)
        
        if not ground_truth or not prediction_result:
            return {"error": "Failed to load data files"}
        
        # Extract prediction text
        prediction_text = ""
        if "model_response" in prediction_result:
            model_resp = prediction_result["model_response"]
            if isinstance(model_resp, dict):
                prediction_text = str(model_resp.get("model_response", "")) + " " + \
                                str(model_resp.get("analysis", ""))
            else:
                prediction_text = str(model_resp)
        
        # Extract structured fields from prediction
        extracted_fields = self.extract_fields_from_prediction(prediction_text)
        
        # Perform evaluations
        field_evaluation = self.evaluate_field_extraction(ground_truth, extracted_fields)
        content_evaluation = self.evaluate_content_accuracy(ground_truth, prediction_text)
        
        # Calculate overall scores
        positioning_score = field_evaluation["overall_metrics"]["f1_score"]
        content_score = (content_evaluation["coverage_ratio"] + content_evaluation["average_similarity"]) / 2
        overall_score = (positioning_score + content_score) / 2
        
        return {
            "ground_truth_file": ground_truth_filename,
            "prediction_file": result_file,
            "evaluation_timestamp": datetime.now().isoformat(),
            "scores": {
                "positioning_score": positioning_score,
                "content_score": content_score,
                "overall_score": overall_score
            },
            "detailed_evaluation": {
                "field_extraction": field_evaluation,
                "content_accuracy": content_evaluation
            },
            "extracted_fields": extracted_fields
        }

    def batch_evaluate(self, result_files: Optional[List[str]] = None) -> Dict[str, Any]:
        """Evaluate multiple result files."""
        
        if result_files is None:
            result_files = [f for f in os.listdir(self.results_dir) if f.endswith('.json')]
        
        all_evaluations = []
        summary_stats = {
            "positioning_scores": [],
            "content_scores": [],
            "overall_scores": []
        }
        
        for result_file in result_files:
            # Try to extract ground truth filename from result filename
            # Assuming naming convention: template_datatype_filename_timestamp.json
            parts = result_file.replace('.json', '').split('_')
            if len(parts) >= 3:
                gt_filename = '_'.join(parts[2:-1])  # Remove template, datatype, and timestamp
            else:
                continue
            
            evaluation = self.evaluate_single_file(gt_filename, result_file)
            
            if "error" not in evaluation:
                all_evaluations.append(evaluation)
                scores = evaluation["scores"]
                summary_stats["positioning_scores"].append(scores["positioning_score"])
                summary_stats["content_scores"].append(scores["content_score"])
                summary_stats["overall_scores"].append(scores["overall_score"])
        
        # Calculate summary statistics
        def calc_stats(scores):
            if not scores:
                return {"mean": 0, "min": 0, "max": 0, "std": 0}
            return {
                "mean": sum(scores) / len(scores),
                "min": min(scores),
                "max": max(scores),
                "std": (sum((x - sum(scores)/len(scores))**2 for x in scores) / len(scores))**0.5
            }
        
        summary = {
            "total_evaluations": len(all_evaluations),
            "positioning_stats": calc_stats(summary_stats["positioning_scores"]),
            "content_stats": calc_stats(summary_stats["content_scores"]),
            "overall_stats": calc_stats(summary_stats["overall_scores"])
        }
        
        return {
            "summary": summary,
            "detailed_evaluations": all_evaluations,
            "evaluation_timestamp": datetime.now().isoformat()
        }

    def save_evaluation_results(self, results: Dict[str, Any], output_filename: str):
        """Save evaluation results to JSON file."""
        output_path = self.evaluation_output_dir / f"{output_filename}.json"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"Evaluation results saved to: {output_path}")
        except Exception as e:
            print(f"Error saving evaluation results: {e}")

    def generate_evaluation_report(self, results: Dict[str, Any]) -> str:
        """Generate a human-readable evaluation report."""
        
        report = []
        report.append("=" * 60)
        report.append("EVALUATION REPORT")
        report.append("=" * 60)
        
        summary = results["summary"]
        report.append(f"Total Evaluations: {summary['total_evaluations']}")
        report.append("")
        
        report.append("OVERALL PERFORMANCE:")
        overall_stats = summary["overall_stats"]
        report.append(f"  Mean Score: {overall_stats['mean']:.3f}")
        report.append(f"  Min Score:  {overall_stats['min']:.3f}")
        report.append(f"  Max Score:  {overall_stats['max']:.3f}")
        report.append(f"  Std Dev:    {overall_stats['std']:.3f}")
        report.append("")
        
        report.append("POSITIONING ACCURACY:")
        pos_stats = summary["positioning_stats"]
        report.append(f"  Mean Score: {pos_stats['mean']:.3f}")
        report.append(f"  Min Score:  {pos_stats['min']:.3f}")
        report.append(f"  Max Score:  {pos_stats['max']:.3f}")
        report.append("")
        
        report.append("CONTENT ACCURACY:")
        content_stats = summary["content_stats"]
        report.append(f"  Mean Score: {content_stats['mean']:.3f}")
        report.append(f"  Min Score:  {content_stats['min']:.3f}")
        report.append(f"  Max Score:  {content_stats['max']:.3f}")
        report.append("")
        
        report.append("TOP PERFORMING FILES:")
        detailed = results["detailed_evaluations"]
        if detailed:
            sorted_results = sorted(detailed, key=lambda x: x["scores"]["overall_score"], reverse=True)
            for i, result in enumerate(sorted_results[:5], 1):
                scores = result["scores"]
                report.append(f"  {i}. {result['prediction_file']}")
                report.append(f"     Overall: {scores['overall_score']:.3f} | "
                            f"Positioning: {scores['positioning_score']:.3f} | "
                            f"Content: {scores['content_score']:.3f}")
        
        return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Evaluate model predictions against ground truth data")
    
    parser.add_argument("--gt-dir", default="../data/data1", 
                       help="Ground truth directory")
    parser.add_argument("--results-dir", default="output", 
                       help="Results directory")
    parser.add_argument("--output-dir", default="evaluation_results", 
                       help="Evaluation output directory")
    parser.add_argument("--result-file", 
                       help="Specific result file to evaluate")
    parser.add_argument("--gt-file", 
                       help="Specific ground truth file to compare against")
    parser.add_argument("--batch", action="store_true", 
                       help="Evaluate all result files in batch")
    
    args = parser.parse_args()
    
    evaluator = FormFieldEvaluator(
        ground_truth_dir=args.gt_dir,
        results_dir=args.results_dir,
        evaluation_output_dir=args.output_dir
    )
    
    try:
        if args.result_file and args.gt_file:
            # Single file evaluation
            result = evaluator.evaluate_single_file(args.gt_file, args.result_file)
            output_name = f"single_eval_{args.result_file}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            evaluator.save_evaluation_results(result, output_name)
            
        elif args.batch:
            # Batch evaluation
            results = evaluator.batch_evaluate()
            output_name = f"batch_evaluation_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            evaluator.save_evaluation_results(results, output_name)
            
            # Generate and print report
            report = evaluator.generate_evaluation_report(results)
            print(report)
            
            # Save report
            report_path = evaluator.evaluation_output_dir / f"{output_name}_report.txt"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\nDetailed report saved to: {report_path}")
        
        else:
            print("Please specify either --batch for batch evaluation or both --result-file and --gt-file for single evaluation")
    
    except Exception as e:
        print(f"Evaluation error: {e}")

if __name__ == "__main__":
    main() 