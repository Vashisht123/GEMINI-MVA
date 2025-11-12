from utils.gemini_setup import get_gemini_model

class CodeAgent:
    def __init__(self):
        # Create a Gemini model instance specifically for code generation
        self.model = get_gemini_model(agent_type="code")

    def handle(self, prompt: str) -> str:
        full_prompt = f"Write code for the following request:\n{prompt}"
        try:
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"CodeAgent error: {e}"
