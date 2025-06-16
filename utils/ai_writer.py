import ast
import re
from utils.prompt_builder import build_key_selection_prompt, build_letter_body_prompt

def select_relevant_keys_with_ai(task, flat_keys, model):
    prompt = build_key_selection_prompt(task, flat_keys)
    response = model(prompt, max_new_tokens=200).strip()

    try:
        match = re.search(r"\[.*?\]", response, re.DOTALL)
        selected = ast.literal_eval(match.group(0)) if match else []
    except:
        selected = []

    return selected

def generate_main_body(task, selected_keys, flat_yaml, model):
    filtered_info = {k: flat_yaml[k] for k in selected_keys if k in flat_yaml}
    context_text = "\n".join(f"{k}: {v}" for k, v in filtered_info.items())
    prompt = build_letter_body_prompt(task, context_text)
    result = model(prompt, max_new_tokens=400).strip()
    return result
