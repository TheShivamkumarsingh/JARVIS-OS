import re

from app.tools.base_tool import BaseTool
from app.tools.safe_math import SafeMath


class CalculatorTool(BaseTool):

     name = "calculator"

     description = "Performs mathematical calculations."

     examples = (
        "25 + 17",
        "What is 18 * 9?",
        "Calculate (20 + 5) * 4",
        "Solve 100 / 5",
     )

     def __init__(self):
        self.math = SafeMath()

     def __init__(self):
        self.math = SafeMath()

     def can_handle(self, command: str) -> bool:
        pattern = r'^[0-9\+\-\*\/\(\)\.\s]+$'
        return bool(re.fullmatch(pattern, command))

     def execute(self, command: str) -> str:
        try:
            result = self.math.evaluate(command)
            return str(result)
        except Exception:
            return "Calculation failed."

        