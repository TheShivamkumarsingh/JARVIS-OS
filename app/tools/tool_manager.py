from app.tools.calculator import CalculatorTool
from app.tools.intent_router import IntentRouter


class ToolManager:

    def __init__(self):

        self.router = IntentRouter()

        self.tools = {
            "calculator": CalculatorTool(),
        }

    def execute(self, command: str):

        tool_name, tool_input = self.router.route(command)

        if tool_name is None:
            return None

        tool = self.tools.get(tool_name)

        if tool:
            return tool.execute(tool_input)

        return None

    def get_tool_metadata(self):

        metadata = {}

        for name, tool in self.tools.items():
            metadata[name] = tool.get_metadata()

        return metadata

    def get_tool_descriptions(self):

        descriptions = []

        for name, tool in self.tools.items():

            metadata = tool.get_metadata()

            description = (
                f"Tool: {metadata['name']}\n"
                f"Description: {metadata['description']}\n"
                f"Examples:\n"
            )

            for example in metadata["examples"]:
                description += f"- {example}\n"

            descriptions.append(description)

        return "\n".join(descriptions)