from app.tools.base_tool import BaseTool
from app.tools.calculator import CalculatorTool
from app.tools.system_info import SystemInfoTool


class ToolManager:

    def __init__(self):

        self.tools: dict[str, BaseTool] = {}

        self.register(CalculatorTool())
        self.register(SystemInfoTool())

    def register(self, tool: BaseTool):

        self.tools[tool.name] = tool

    def execute(self, command: str):

        for tool in self.tools.values():

            if tool.can_handle(command):

                return tool.execute(command)

        return None

    def get_tool_metadata(self):

        metadata = {}

        for name, tool in self.tools.items():

            metadata[name] = tool.get_metadata()

        return metadata

    def get_tool_descriptions(self):

        descriptions = []

        for tool in self.tools.values():

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