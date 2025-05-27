def main():
    # Get user input and clean it up
    greeting_input = input("Greeting: ").strip().lower()

    # Pass the greeting to the value function and store the result
    result = value(greeting_input)

    # Print the output
    print(f"Output: ${result}")


def value(greeting):

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
