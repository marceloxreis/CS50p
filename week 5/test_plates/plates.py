def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # Check for basic length requirements
    if not (2 <= len(plate) <= 6):
        return False

    # Ensure the plate starts with letters
    if not plate[0:2].isalpha():
        return False

    # Ensure no invalid characters (only letters and digits allowed)
    if not plate.isalnum():
        return False

    # Flag to track if we've encountered a number
    number_started = False

    for i, char in enumerate(plate):
        if char.isdigit():
            # If it's the first number, ensure it's not '0'
            if number_started is False and char == '0':
                return False
            number_started = True
        elif char.isalpha():
            # If a letter appears after a number, it's invalid
            if number_started:
                return False

    return True

if __name__ == "__main__":
    main()
