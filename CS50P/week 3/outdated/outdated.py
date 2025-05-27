# List of valid months and their corresponding calendar numbers
month_to_number = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

def is_valid_date(month, day):
    return 1 <= month <= 12 and 1 <= day <= 31

while True:
    try:
        date = input("Date: ")

        # Case 1: Input is in the format month/day/year (e.g., 12/25/2025)
        if '/' in date:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)

            if is_valid_date(month, day):
                print(f"{year}-{month:02d}-{day:02d}")
                break  # Exit the loop
            else:
                print("Invalid date. Please try again.")
                continue  # Skip to the next iteration

        # Case 2: Input is in the format Month day, year (e.g., January 25, 2025)
        elif ',' in date:
            parts = date.split(', ')
            if len(parts) == 2:
                month_day = parts[0].title()  # Ensure the month is capitalized
                year = parts[1]

                # Split the month_day into month and day
                month_str, day = month_day.split(' ')
                day = int(day)  # Convert day to integer

                if month_str in month_to_number:
                    month_number = month_to_number[month_str]
                    year = int(year)  # Convert year to integer

                    if is_valid_date(month_number, day):
                        print(f"{year}-{month_number:02d}-{day:02d}")
                        break  # Exit the loop
                    else:
                        print("Invalid date. Please try again.")
                        continue  # Skip to the next iteration
                else:
                    print("Invalid date. Please try again.")
                    continue  # Skip to the next iteration

        else:
            print("Invalid date. Please try again.")
            continue  # Skip to the next iteration

    except ValueError:
        print("Invalid date. Please try again.")
        continue  # Skip to the next iteration
