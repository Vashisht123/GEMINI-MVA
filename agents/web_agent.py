from utils.gemini_setup import get_gemini_model
import requests

class WebAgent:
    def __init__(self):
        self.model = get_gemini_model(agent_type="text")

    def handle(self, prompt: str) -> str:
        try:
            # Optional: use Gemini to summarize prompt / info
            response = self.model.generate_content(f"Provide information about: {prompt}")
            return response.text.strip()
        except Exception as e:
            return f"WebAgent error: {e}"
