import re

from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):

    def can_handle(self, command: str) -> bool:

        pattern = r'^[0-9\+\-\*\/\(\)\.\s]+$'

        return bool(re.fullmatch(pattern, command))

    def execute(self, command: str) -> str:

        try:

            result = eval(command)

            return str(result)

        except Exception:

            return "Calculation failed."