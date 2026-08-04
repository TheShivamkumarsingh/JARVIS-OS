from app.models.llm import LLM


class LLMService:
    def __init__(self):
        self.llm = LLM()

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        return self.llm.generate(system_prompt, user_prompt)