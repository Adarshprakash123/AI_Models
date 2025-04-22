import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Load API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Check available models
models = genai.list_models()

for model in models:
    print(model.name)