from utils.memory import Memory
from agents.coordinator import Coordinator

def run_console():
    print("🤖 Multi-Agent Assistant (Gemini). Type 'exit' or 'quit' to stop.\n")
    memory = Memory()
    coordinator = Coordinator(memory)

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            break

        try:
            result = coordinator.route(user_input)
            print(f"[{result['agent'].upper()}] {result['text']}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")

if __name__ == "__main__":
    run_console()
