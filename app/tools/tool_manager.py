from app.tools.calculator import CalculatorTool


class ToolManager:

    def __init__(self):

        self.tools = [
            CalculatorTool()
        ]

    def execute(self, command: str):

        for tool in self.tools:

            if tool.can_handle(command):

                return tool.execute(command)

        return None