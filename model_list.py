import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found")

# Configure Gemini
genai.configure(api_key=api_key)

# List models
print("\nAvailable Google Gemini Models:\n")

for model in genai.list_models():
    # Show only models that support text generation
    if "generateContent" in model.supported_generation_methods:
        print(f"- {model.name}")
