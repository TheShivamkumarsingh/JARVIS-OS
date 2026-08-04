from app.memory.memory import Memory


class MemoryService:
    def __init__(self):
        self.memory = Memory()

    def save_profile(self, key: str, value: str):
        self.memory.save_profile(key, value)

    def get_profile(self, key: str):
        return self.memory.get_profile(key)

    def get_all_profile(self):
        return self.memory.get_all_profile()

    def remember(self, user_message: str, assistant_message: str):
        self.memory.remember(user_message, assistant_message)

    def get_history(self):
        return self.memory.get_history()

    def close(self):
        self.memory.close()