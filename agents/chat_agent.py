from utils.gemini_setup import get_gemini_model

class ChatAgent:
    def __init__(self):
        self.model = get_gemini_model(agent_type="chat")

    def handle(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"ChatAgent error: {e}"
