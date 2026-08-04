from pathlib import Path
import json

from app.services.llm_service import LLMService


class MemoryExtractor:

    def __init__(self):
        self.llm = LLMService()

        prompt_path = (
            Path(__file__).resolve().parents[1]
            / "prompts"
            / "memory_prompt.txt"
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.prompt = file.read()

    def extract(self, message):

        response = self.llm.generate(
            self.prompt,
            message
        ).strip()

        if response == "NONE":
            return None

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return None