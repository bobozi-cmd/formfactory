import os
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional
import subprocess
import base64
from datetime import datetime

import sys
sys.path.append('.')
from model_call import ModelCaller

class BatchProcessor:
    def __init__(self, 
                 data_dir: str = "../data",
                 output_dir: str = "output",
                 template_dir: str = "prompt_template"):
        """
        Initialize the batch processor.
        
        Args:
            data_dir (str): Path to the data directory
            output_dir (str): Path to save output JSON files
            template_dir (str): Path to prompt templates
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = template_dir
        self.model_caller = ModelCaller(template_dir=template_dir)
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)
        
        # Mapping of data types to their directories
        self.data_mappings = {
            "json": self.data_dir / "data1",
            "text": self.data_dir / "data2",
            "labeled_images": self.data_dir / "labeled-images"
        }

    def get_available_data_files(self, data_type: str) -> List[str]:
        """Get list of available data files for a given type."""
        if data_type not in self.data_mappings:
            return []
        
        data_path = self.data_mappings[data_type]
        if not data_path.exists():
            return []
        
        if data_type == "labeled_images":
            # For labeled images, return category folders
            return [d.name for d in data_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
        else:
            # For json and text files
            extensions = {".json"} if data_type == "json" else {".txt"}
            return [f.stem for f in data_path.iterdir() 
                   if f.suffix in extensions and not f.name.startswith('.')]

    def load_data_content(self, data_type: str, filename: str) -> Optional[Dict[str, Any]]:
        """Load content from data files."""
        try:
            if data_type == "json":
                file_path = self.data_mappings[data_type] / f"{filename}.json"
                with open(file_path, 'r', encoding='utf-8') as f:
                    return {"type": "json", "content": json.load(f)}
            
            elif data_type == "text":
                file_path = self.data_mappings[data_type] / f"{filename}.txt"
                with open(file_path, 'r', encoding='utf-8') as f:
                    return {"type": "text", "content": f.read()}
            
            elif data_type == "labeled_images":
                # For labeled images, load both images and labels from a category folder
                category_path = self.data_mappings[data_type] / filename
                if not category_path.exists():
                    return None
                
                images_and_labels = []
                for img_file in category_path.glob("*.png"):
                    label_file = img_file.with_suffix('.txt')
                    
                    # Encode image to base64
                    with open(img_file, 'rb') as f:
                        img_data = base64.b64encode(f.read()).decode('utf-8')
                    
                    # Load label if exists
                    label_data = ""
                    if label_file.exists():
                        with open(label_file, 'r', encoding='utf-8') as f:
                            label_data = f.read()
                    
                    images_and_labels.append({
                        "image_name": img_file.name,
                        "image_data": img_data,
                        "label_data": label_data
                    })
                
                return {
                    "type": "labeled_images",
                    "category": filename,
                    "content": images_and_labels
                }
        
        except Exception as e:
            print(f"Error loading {data_type}/{filename}: {e}")
            return None

    def prepare_prompt(self, template_name: str, data_content: Dict[str, Any]) -> str:
        """Prepare the prompt by combining template with data content."""
        try:
            # Load the template
            template = self.model_caller.load_template(template_name)
            
            # Format the prompt with data content
            if data_content["type"] == "json":
                data_str = json.dumps(data_content["content"], indent=2)
                prompt = f"{template}\n\nData to analyze (JSON format):\n{data_str}"
            
            elif data_content["type"] == "text":
                prompt = f"{template}\n\nData to analyze (Text format):\n{data_content['content']}"
            
            elif data_content["type"] == "labeled_images":
                prompt = f"{template}\n\nData to analyze (Labeled Images):\n"
                prompt += f"Category: {data_content['category']}\n"
                prompt += f"Number of images: {len(data_content['content'])}\n\n"
                
                for item in data_content['content']:
                    prompt += f"Image: {item['image_name']}\n"
                    prompt += f"Labels: {item['label_data']}\n"
                    prompt += f"Image data (base64): {item['image_data'][:100]}...\n\n"
            
            return prompt
        
        except Exception as e:
            print(f"Error preparing prompt: {e}")
            return ""

    def call_model_api(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Call the model API using the existing ModelCaller."""
        try:
            # Use the existing model caller
            response = self.model_caller.call_model(prompt, **kwargs)
            
            # TODO: Replace this with actual API call when implemented
            # For now, simulate a response
            simulated_response = {
                "model_response": "This is a simulated model response for the provided data.",
                "analysis": "The model would analyze the content and provide insights here.",
                "confidence": 0.85,
                "timestamp": datetime.now().isoformat(),
                "prompt_length": len(prompt),
                "status": "success"
            }
            
            return simulated_response
        
        except Exception as e:
            return {
                "error": str(e),
                "status": "failed",
                "timestamp": datetime.now().isoformat()
            }

    def save_results(self, results: Dict[str, Any], output_filename: str):
        """Save results to a JSON file."""
        output_path = self.output_dir / f"{output_filename}.json"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"Results saved to: {output_path}")
        except Exception as e:
            print(f"Error saving results: {e}")

    def process_single_item(self, 
                           template_name: str,
                           data_type: str, 
                           filename: str,
                           **model_kwargs) -> Dict[str, Any]:
        """Process a single data item with the specified template."""
        print(f"Processing {data_type}/{filename} with template {template_name}...")
        
        # Load data content
        data_content = self.load_data_content(data_type, filename)
        if not data_content:
            return {"error": f"Failed to load {data_type}/{filename}"}
        
        # Prepare prompt
        prompt = self.prepare_prompt(template_name, data_content)
        if not prompt:
            return {"error": "Failed to prepare prompt"}
        
        # Call model API
        model_response = self.call_model_api(prompt, **model_kwargs)
        
        # Prepare complete results
        results = {
            "template_used": template_name,
            "data_type": data_type,
            "data_source": filename,
            "prompt_preview": prompt[:500] + "..." if len(prompt) > 500 else prompt,
            "model_response": model_response,
            "processing_timestamp": datetime.now().isoformat()
        }
        
        return results

    def process_batch(self, 
                     template_name: str,
                     data_type: str,
                     filenames: Optional[List[str]] = None,
                     **model_kwargs):
        """Process multiple data items in batch."""
        if filenames is None:
            filenames = self.get_available_data_files(data_type)
        
        if not filenames:
            print(f"No files found for data type: {data_type}")
            return
        
        print(f"Starting batch processing of {len(filenames)} files...")
        
        all_results = []
        for filename in filenames:
            result = self.process_single_item(template_name, data_type, filename, **model_kwargs)
            all_results.append(result)
        
        # Save batch results
        batch_output_name = f"batch_{template_name}_{data_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.save_results({
            "batch_info": {
                "template": template_name,
                "data_type": data_type,
                "total_processed": len(all_results),
                "timestamp": datetime.now().isoformat()
            },
            "results": all_results
        }, batch_output_name)

def main():
    parser = argparse.ArgumentParser(description="Batch process data files with language model API")
    
    parser.add_argument("template", help="Template name to use for processing")
    parser.add_argument("data_type", choices=["json", "text", "labeled_images"], 
                       help="Type of data to process")
    parser.add_argument("--filename", help="Specific filename to process (optional)")
    parser.add_argument("--data-dir", default="../data", help="Data directory path")
    parser.add_argument("--output-dir", default="output", help="Output directory path")
    parser.add_argument("--template-dir", default="prompt_template", help="Template directory path")
    parser.add_argument("--list-data", action="store_true", help="List available data files")
    parser.add_argument("--list-templates", action="store_true", help="List available templates")
    
    args = parser.parse_args()
    
    processor = BatchProcessor(
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        template_dir=args.template_dir
    )
    
    if args.list_templates:
        print("Available templates:")
        for template in processor.model_caller.available_templates:
            print(f"  - {template}")
        return
    
    if args.list_data:
        for data_type in ["json", "text", "labeled_images"]:
            files = processor.get_available_data_files(data_type)
            print(f"{data_type.upper()} files ({len(files)}):")
            for file in files[:10]:  # Show first 10
                print(f"  - {file}")
            if len(files) > 10:
                print(f"  ... and {len(files) - 10} more")
            print()
        return
    
    # Process single file or batch
    try:
        if args.filename:
            result = processor.process_single_item(args.template, args.data_type, args.filename)
            output_name = f"{args.template}_{args.data_type}_{args.filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            processor.save_results(result, output_name)
        else:
            processor.process_batch(args.template, args.data_type)
    
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == "__main__":
    main() 