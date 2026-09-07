import re


class IntentRouter:
    """
    Detects user intent and extracts tool-specific input.
    """

    MATH_PATTERNS = [
        r"what is (.+)",
        r"calculate (.+)",
        r"solve (.+)",
        r"how much is (.+)",
    ]

    def route(self, message: str):
        message = message.lower().strip()
        message = message.rstrip("?.!,")
        # Pure mathematical expression
        if re.fullmatch(r"[0-9+\-*/().\s]+", message):
            return ("calculator", message)

        # Natural language
        for pattern in self.MATH_PATTERNS:
            match = re.match(pattern, message)

            if match:
                expression = match.group(1).strip()
                expression = expression.rstrip("?.!,")
                
                if re.fullmatch(r"[0-9+\-*/().\s]+", expression):
                    return ("calculator", expression)

        return (None, message)