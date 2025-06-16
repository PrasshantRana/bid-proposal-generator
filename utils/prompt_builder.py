def build_key_selection_prompt(task_description, flat_keys):
    key_list_text = "\n".join(f"- {key}" for key in flat_keys)
    return f"""
Task: {task_description}

Available YAML Keys:
{key_list_text}

Instructions:
- Select only the keys needed to write the main body of the tender proposal letter.
- Return ONLY a Python list. No explanation or additional text.
"""



def build_letter_body_prompt(task_description, context_text):
    return f"""
You are an expert in writing formal tender proposal responses.

Task: {task_description}

Context:
{context_text}

Write the main body of the proposal letter in a professional and clear tone. without salutations or closings.
Make sure to include only relevant information from the context provided.
"""

