import yaml

file_path = "C:/Users/devic/bid-proposal-generator/input/instructions.yaml"

def load_yaml(file_path):
    """Load YAML file and return data as a Python dictionary."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)