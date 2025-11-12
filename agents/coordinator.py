from agents.chat_agent import ChatAgent
from agents.code_agent import CodeAgent
from agents.planner_agent import PlannerAgent
from agents.web_agent import WebAgent

class Coordinator:
    def __init__(self, memory):
        self.memory = memory
        self.chat_agent = ChatAgent()
        self.code_agent = CodeAgent()
        self.planner_agent = PlannerAgent()
        self.web_agent = WebAgent()

    def route(self, text: str):
        text_lower = text.lower()
        self.memory.add("user", text)

        if any(k in text_lower for k in ["code", "python", "error", "program"]):
            result = self.code_agent.handle(text)
            agent_name = "code"
        elif any(k in text_lower for k in ["plan", "schedule", "todo", "day", "reminder"]):
            result = self.planner_agent.handle(text)
            agent_name = "planner"
        elif any(k in text_lower for k in ["search", "find", "lookup", "news"]):
            result = self.web_agent.handle(text)
            agent_name = "web"
        else:
            result = self.chat_agent.handle(text)
            agent_name = "chat"

        self.memory.add(agent_name, result)
        return {"agent": agent_name, "text": result}
