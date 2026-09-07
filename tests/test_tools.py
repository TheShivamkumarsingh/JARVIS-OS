from app.tools.tool_manager import ToolManager

manager = ToolManager()

tests = [
    "25+17",
    "What is 18*9?",
    "Calculate (20+5)*4",
    "Solve 100/5",
    "How much is 12*12?",
    "Hello",
]

for test in tests:
    print(f"Input : {test}")
    print(f"Output: {manager.execute(test)}")
    print("-" * 40)