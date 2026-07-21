from app.brain.brain import Brain
from app.memory.memory import Memory


class Assistant:
    def __init__(self):
        self.brain = Brain()
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

            self.memory.remember(user_input)

            response = self.brain.think(user_input)

            print(f"\nJARVIS: {response}")