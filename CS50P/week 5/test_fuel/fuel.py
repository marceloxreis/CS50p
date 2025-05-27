def convert(fraction):
    try:
        numerator, denominator = fraction.split('/')
        numerator = int(numerator)
        denominator = int(denominator)

        if denominator == 0:
            raise ZeroDivisionError
        if numerator > denominator:
            raise ValueError

        return round((numerator / denominator) * 100)
    except ValueError:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        try:
            fuel = input("Fraction: ")
            percentage = convert(fuel)
            status = gauge(percentage)
            print(status)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input.")

if __name__ == "__main__":
    main()
