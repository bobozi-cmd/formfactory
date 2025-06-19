import argparse
import os
import json
from typing import Optional, Dict, Any

class ModelCaller:
    def __init__(self, template_dir: str = "eval/prompt_template"):
        """
        Initialize the ModelCaller with the template directory path.
        
        Args:
            template_dir (str): Path to the directory containing prompt templates
        """
        self.template_dir = template_dir
        self.available_templates = self._get_available_templates()

    def _get_available_templates(self) -> list:
        """Get a list of available template names without the .txt extension."""
        templates = []
        for file in os.listdir(self.template_dir):
            if file.endswith('.txt') and not file.startswith('.'):
                templates.append(file[:-4])  # Remove .txt extension
        return sorted(templates)

    def load_template(self, template_name: str) -> str:
        """
        Load the content of the specified template.
        
        Args:
            template_name (str): Name of the template without .txt extension
            
        Returns:
            str: Content of the template file
            
        Raises:
            FileNotFoundError: If template doesn't exist
        """
        template_path = os.path.join(self.template_dir, f"{template_name}.txt")
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template {template_name} not found")
        
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()

    def call_model(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """
        Call the model with the given prompt and additional parameters.
        This is a placeholder function that would be implemented with actual API calls.
        
        Args:
            prompt (str): The prompt to send to the model
            **kwargs: Additional parameters for the model
            
        Returns:
            Dict[str, Any]: Model response
        """
        # TODO: Implement actual model API call
        # Example implementation would look like:
        # response = api.completion.create(
        #     model="gpt-4",
        #     prompt=prompt,
        #     **kwargs
        # )
        # return response
        
        print(f"[DEBUG] Would call model with prompt: {prompt[:100]}...")
        return {"status": "success", "message": "Model call placeholder"}

def main():
    parser = argparse.ArgumentParser(description="Call language model with specified template")
    parser.add_argument(
        "template",
        help="Name of the template to use (without .txt extension)"
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List all available templates"
    )
    parser.add_argument(
        "--template-dir",
        default="prompt_template",
        help="Directory containing prompt templates"
    )
    
    args = parser.parse_args()
    
    caller = ModelCaller(template_dir=args.template_dir)
    
    if args.list_templates:
        print("Available templates:")
        for template in caller.available_templates:
            print(f"  - {template}")
        return
    
    try:
        # Load the template
        prompt = caller.load_template(args.template)
        
        # Call the model
        response = caller.call_model(prompt)
        
        # Print the response
        print(json.dumps(response, indent=2))
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Use --list-templates to see available templates")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main() 