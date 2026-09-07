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