import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", None)
LITELLM_API_KEY = os.getenv("LITELLM_API_KEY", None)
LITELLM_BASE_URL = os.getenv("LITELLM_BASE_URL", None)

PROXY = os.getenv("PROXY", None)
PROXY_AUTH = os.getenv("PROXY_AUTH", None)

# Load litellm models from yaml model list
litellm_model_yaml_path = "litellm_model_list.yaml"
if os.path.exists(litellm_model_yaml_path):
    import yaml

    with open(litellm_model_yaml_path, "r") as file:
        litellm_model_list = yaml.safe_load(file)["models"]

        # Add the api_key and base_url to each model
        for model in litellm_model_list:
            model["litellm_params"]["api_key"] = LITELLM_API_KEY
            model["litellm_params"]["api_base"] = LITELLM_BASE_URL

else:
    litellm_model_list = []
