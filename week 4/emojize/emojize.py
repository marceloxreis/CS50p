
import emoji

def main():
    # Prompt the user for input
    user_input = input("Input: ")

    # Convert the input to emojized text
    emojized_text = emoji.emojize(user_input, language="alias")

    # Output the emojized text
    print("Output:", emojized_text)

if __name__ == "__main__":
    main()
