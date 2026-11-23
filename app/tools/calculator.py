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

    MATH_PATTERNS = (
        r"what is (.+)",
        r"calculate (.+)",
        r"solve (.+)",
        r"how much is (.+)",
    )

    EXPRESSION_PATTERN = r"[0-9+\-*/().\s]+"

    def __init__(self):
        self.math = SafeMath()

    def can_handle(self, command: str) -> bool:

        message = command.lower().strip()
        message = message.rstrip("?.!,")

        if re.fullmatch(self.EXPRESSION_PATTERN, message):
            return True

        for pattern in self.MATH_PATTERNS:

            match = re.fullmatch(pattern, message)

            if match:

                expression = match.group(1).strip()
                expression = expression.rstrip("?.!,")

                if re.fullmatch(
                    self.EXPRESSION_PATTERN,
                    expression
                ):
                    return True

        return False

    def execute(self, command: str) -> str:

        message = command.lower().strip()
        message = message.rstrip("?.!,")

        if re.fullmatch(self.EXPRESSION_PATTERN, message):

            expression = message

        else:

            expression = None

            for pattern in self.MATH_PATTERNS:

                match = re.fullmatch(pattern, message)

                if match:

                    candidate = match.group(1).strip()
                    candidate = candidate.rstrip("?.!,")

                    if re.fullmatch(
                        self.EXPRESSION_PATTERN,
                        candidate
                    ):
                        expression = candidate
                        break

        if expression is None:
            return "Calculation failed."

        try:

            result = self.math.evaluate(expression)

            return str(result)

        except Exception:

            return "Calculation failed."