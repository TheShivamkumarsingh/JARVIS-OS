from pathlib import Path

from app.services.llm_service import LLMService


class Brain:

    def __init__(self):

        self.llm = LLMService()

        prompt_path = (
            Path(__file__).resolve().parents[1]
            / "prompts"
            / "system_prompt.txt"
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def think(self, context: str):

        return self.llm.generate(
            self.system_prompt,
            context
        )