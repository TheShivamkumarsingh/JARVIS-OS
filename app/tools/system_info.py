import platform

from app.tools.base_tool import BaseTool


class SystemInfoTool(BaseTool):

    name = "system_info"

    description = (
        "Provides information about the operating system, "
        "Python version, machine architecture, and processor."
    )

    examples = (
        "What operating system am I using?",
        "What platform am I on?",
        "What Python version am I using?",
        "What is my computer architecture?",
        "What processor am I using?",
    )

    def can_handle(self, command: str) -> bool:

        message = command.lower().strip()

        patterns = (
            "what operating system am i using",
            "what operating system am i on",
            "what os am i using",
            "what os am i on",
            "what platform am i on",
            "what python version am i using",
            "what python version do i have",
            "what is my computer architecture",
            "what is my architecture",
            "what processor am i using",
            "what cpu am i using",
        )

        return message.rstrip("?.!,") in patterns

    def execute(self, command: str) -> str:

        message = command.lower().strip()
        message = message.rstrip("?.!,")

        if "python version" in message:
            return f"Python version: {platform.python_version()}"

        if "architecture" in message:
            return f"Architecture: {platform.machine()}"

        if "processor" in message or "cpu" in message:
            processor = platform.processor()

            if not processor:
                processor = "Unknown"

            return f"Processor: {processor}"

        if "platform" in message:
            return f"Platform: {platform.platform()}"

        if "operating system" in message or "what os" in message:
            return f"Operating system: {platform.system()}"

        return "System information unavailable."