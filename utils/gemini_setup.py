import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model(agent_type="chat"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Set it in Streamlit secrets or .env")

    genai.configure(api_key=api_key)

    if agent_type == "chat":
        model_name = "gemini-2.5-flash"
    elif agent_type == "code":
        model_name = "gemini-2.5-pro"
    else:
        model_name = "gemini-2.5-flash"

    return genai.GenerativeModel(model_name)
