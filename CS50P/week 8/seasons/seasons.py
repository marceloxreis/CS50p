from datetime import date
import inflect
import sys

def main():
    birth_date = get_birth_date()

    minutes_lived = calculate_minutes_lived(birth_date)
    words = convert_to_words(minutes_lived)
    print(f"{words} minutes")

def get_birth_date():
    while True:
        try:
            birth_date = input("Date of Birth (YYYY-MM-DD): ")
            return date.fromisoformat(birth_date)
        except ValueError:
            sys.exit(1)

def calculate_minutes_lived(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60 



def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return words[0].upper() + words[1:]

if __name__ == "__main__":
    main()
