from abc import ABC, abstractmethod


class BaseTool(ABC):

    name: str = ""
    description: str = ""
    examples: tuple[str, ...] = ()

    @abstractmethod
    def can_handle(self, command: str) -> bool:
        """Return True if this tool can handle the command."""
        pass

    @abstractmethod
    def execute(self, command: str) -> str:
        """Execute the command and return the result."""
        pass

    def get_metadata(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "examples": self.examples,
        }