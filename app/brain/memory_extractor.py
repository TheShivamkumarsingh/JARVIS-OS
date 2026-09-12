from pathlib import Path
import json

from app.services.llm_service import LLMService


class MemoryExtractor:

    ALLOWED_KEYS = {
        "name",
        "favorite_language",
        "current_project",
    }

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

            data = json.loads(response)

        except json.JSONDecodeError:

            return None

        if not isinstance(data, dict):
            return None

        if data.get("remember") is not True:
            return None

        key = data.get("key")
        value = data.get("value")

        if key not in self.ALLOWED_KEYS:
            return None

        if not isinstance(value, str):
            return None

        value = value.strip()

        if not value:
            return None

        return {
            "remember": True,
            "key": key,
            "value": value,
        }
