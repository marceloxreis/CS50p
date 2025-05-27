import random
import string

def main():
    include_symbols = function_symbols()
    password = function_str(function_length(), include_symbols)
    print(password)
def function_length():
    while True:
        length = input("What's the length you want? ")

        try:
            length = int(length)
            if length <= 0:
                print("The length needs to be bigger than 0.")
            elif length > 15:
                print("The max capacity of this generator is 15 characters.")
            else:
                return length
        except ValueError:
            print("The length needs to be a number.")

def function_str(length, include_symbols):
    if include_symbols:
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, numbers, symbols
    else:
        characters = string.ascii_letters + string.digits  # Only letters and numbers

    random_password = "".join(random.sample(characters, length))  # Avoids repetition and shuffling issue
    return random_password

def function_symbols():
    while True:
        symbols = input("Do you need symbols in your password? (Y/N) ").strip().lower()
        if symbols in ("y", "yes"):
            return True
        elif symbols in ("n", "no"):
            return False
        else:
            print("Invalid input, please enter Y/N.")

if __name__ == "__main__":
    main()
