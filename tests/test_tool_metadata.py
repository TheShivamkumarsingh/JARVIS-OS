from app.tools.calculator import CalculatorTool


def main():

    calculator = CalculatorTool()

    metadata = calculator.get_metadata()

    print("========== TOOL METADATA ==========")

    print("Name:", metadata["name"])
    print("Description:", metadata["description"])

    print("Examples:")

    for example in metadata["examples"]:
        print("-", example)


if __name__ == "__main__":
    main()