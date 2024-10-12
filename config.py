import ollama

class Config:
    PAGE_TITLE = "Luna's Tech Lounge 🔥💋💻"
    DEFAULT_MODEL = "llama3.2:latest"

    # Retrieve the list of models using ollama.list()
    models_info = ollama.list()
    # Access the list of models
    model_list = models_info['models']
    # Extract the model names
    OLLAMA_MODELS = tuple(model['name'] for model in model_list)