from app.tools.system_info import SystemInfoTool


def main():

    tool = SystemInfoTool()

    tests = [
        "What operating system am I using?",
        "What Python version am I using?",
        "What is my computer architecture?",
        "What processor am I using?",
    ]

    for command in tests:

        print(f"\nCommand: {command}")
        print(f"Can handle: {tool.can_handle(command)}")
        print(f"Result: {tool.execute(command)}")


if __name__ == "__main__":
    main()
    