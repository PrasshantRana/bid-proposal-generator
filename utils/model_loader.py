from ctransformers import AutoModelForCausalLM

def load_mistral_model(model_path, gpu_layers=0):
    return AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="mistral",
        gpu_layers=gpu_layers
    )
