from utils.yaml_loader import load_yaml
from utils.ai_writer import generate_main_body
from utils.doc_writer import render_to_docx

def main():
    yaml_path = "input/instructions.yaml"
    template_path = "templates/sample_template.docx"
    output_path = "output/submission_letter.docx"

    # Load YAML data
    data = load_yaml(yaml_path)

    # Generate letter body using AI
    content = generate_main_body(data)

    # Render content into .docx template
    render_to_docx(template_path, output_path, {"content": content})

if __name__ == "__main__":
    main()

