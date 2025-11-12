from utils.gemini_setup import get_gemini_model

class PlannerAgent:
    def __init__(self):
        self.model = get_gemini_model(agent_type="text")

    def handle(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(f"Create a plan: {prompt}")
            return response.text.strip()
        except Exception as e:
            return f"PlannerAgent error: {e}"
