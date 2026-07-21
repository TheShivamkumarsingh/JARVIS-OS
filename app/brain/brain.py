from pathlib import Path

from app.models.llm import LLM


class Brain:

    def __init__(self):

        self.llm = LLM()

        prompt_path = (
            Path(__file__).resolve().parents[1]
            / "prompts"
            / "system_prompt.txt"
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def think(self, message):

        return self.llm.generate(
            self.system_prompt,
            message
        )