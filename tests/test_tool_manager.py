from app.tools.tool_manager import ToolManager


def main():

    manager = ToolManager()

    metadata = manager.get_tool_metadata()

    print("========== REGISTERED TOOLS ==========")

    for name, info in metadata.items():

        print("\nTool:", name)
        print("Description:", info["description"])

        print("Examples:")

        for example in info["examples"]:
            print("-", example)


if __name__ == "__main__":
    main()