# utils/gemini_setup.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model(agent_type="chat"):
    """Return a Gemini model instance for a given agent type."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment or .env")

    genai.configure(api_key=api_key)

    # Choose valid model names
    if agent_type == "chat":
        model_name = "gemini-2.5-flash"  # replace with an available Gemini model
    elif agent_type == "code":
        model_name = "gemini-2.5-pro"
    else:
        model_name = "gemini-2.5-flash"

    # Create a GenerativeModel instance
    return genai.GenerativeModel(model_name)
