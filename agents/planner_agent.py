from utils.gemini_setup import get_gemini_model

class PlannerAgent:
    def __init__(self):
        self.model = get_gemini_model(agent_type="text")

    def handle(self, prompt: str) -> str:
        full_prompt = f"Create a plan for: {prompt}"
        try:
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"PlannerAgent error: {e}"
