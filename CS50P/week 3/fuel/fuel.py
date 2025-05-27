def get_fuel_fraction():
    """Prompt user for a valid fuel fraction."""
    while True:
        try:
            fuel = input("Fraction: ")
            numerator, denominator = fuel.split('/')
            numerator = int(numerator)
            denominator = int(denominator)

            if denominator == 0:
                raise ZeroDivisionError
            if numerator > denominator:
                raise ValueError
            return numerator, denominator
        except ValueError:
            print("Invalid input. Please enter a fraction in the form 'numerator/denominator'.")
        except ZeroDivisionError:
            print("Invalid input. Denominator cannot be zero.")

def calculate_percentage(numerator, denominator):
    """Convert fraction to percentage."""
    return round((numerator / denominator) * 100)

def determine_fuel_status(percentage):
    """Determine the fuel status based on percentage."""
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    """Main function to run the fuel program."""
    numerator, denominator = get_fuel_fraction()
    percentage = calculate_percentage(numerator, denominator)
    status = determine_fuel_status(percentage)
    print(status)

if __name__ == "__main__":
    main()
