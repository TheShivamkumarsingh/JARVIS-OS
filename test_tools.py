from app.tools.tool_manager import ToolManager

manager = ToolManager()

tests = [
    "25+17",
    "18*9",
    "(20+5)*4",
    "Hello",
    "Who am I?"
]

for test in tests:

    print(test)

    print(manager.execute(test))

    print("-" * 30)