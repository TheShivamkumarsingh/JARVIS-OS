from app.brain.brain import Brain
from app.memory.memory import Memory
from app.conversation.engine import ConversationEngine

class Assistant:
    def __init__(self):
        self.engine = ConversationEngine()
        self.memory = Memory()

    def chat(self):
        print("=" * 50)
        print("🤖 JARVIS v1.0")
        print("Type 'exit' to quit.")
        print("=" * 50)

        while True:
            user_input = input("\nYou: ")

            if user_input.lower() == "exit":
                print("\nJARVIS: Goodbye! Have a great day.")
                break

    

            response = self.engine.process(user_input)

            print(f"\nJARVIS: {response}")