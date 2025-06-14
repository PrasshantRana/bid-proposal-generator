from docxtpl import DocxTemplate

def render_to_docx(template_path, output_path, context):
    """
    Renders a Word document by filling in the placeholders
    using the given context dictionary.
    """
    doc = DocxTemplate(template_path)
    doc.render(context)
    doc.save(output_path)

