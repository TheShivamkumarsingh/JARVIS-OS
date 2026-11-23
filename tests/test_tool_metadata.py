
from app.tools.tool_manager import ToolManager


def main():

    manager = ToolManager()

    metadata = manager.get_tool_metadata()

    print("========== TOOL METADATA ==========")

    for name, details in metadata.items():

        print(f"\nName: {details['name']}")
        print(f"Description: {details['description']}")

        print("Examples:")

        for example in details["examples"]:
            print("-", example)


if __name__ == "__main__":
    main()
