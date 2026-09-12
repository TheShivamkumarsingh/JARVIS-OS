from app.context.context_builder import ContextBuilder
from app.tools.tool_manager import ToolManager


def main():

    tools = ToolManager()

    builder = ContextBuilder(tools)

    context = builder.build_context(
        "Who am I?"
    )

    print("========== GENERATED CONTEXT ==========")
    print(context)


if __name__ == "__main__":
    main()