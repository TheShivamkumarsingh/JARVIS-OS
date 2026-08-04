from pathlib import Path

from app.brain.memory_extractor import MemoryExtractor
from app.services.llm_service import LLMService
from app.services.memory_service import MemoryService


class Brain:

    def __init__(self):

        self.llm = LLMService()
        self.memory = MemoryService()
        self.extractor = MemoryExtractor()

        prompt_path = (
            Path(__file__).resolve().parents[1]
            / "prompts"
            / "system_prompt.txt"
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def think(self, message):

        # -------- Memory Extraction --------

        memory = self.extractor.extract(message)

        if memory:

            self.memory.save_profile(
                memory["key"],
                memory["value"]
            )

        # -------- Chat --------

        response = self.llm.generate(
            self.system_prompt,
            message
        )

        # -------- Save Conversation --------

        self.memory.remember(
            message,
            response
        )

        return response