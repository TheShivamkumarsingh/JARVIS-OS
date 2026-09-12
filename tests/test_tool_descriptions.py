from app.tools.tool_manager import ToolManager


def main():

    manager = ToolManager()

    descriptions = manager.get_tool_descriptions()

    print("========== TOOL DESCRIPTIONS ==========")
    print(descriptions)


if __name__ == "__main__":
    main()