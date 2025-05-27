import sys
import os
import csv

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    check(input_file)
    process(input_file, output_file)

def check(file_name):
    if not file_name.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)

    if not os.path.exists(file_name):
        print("File does not exist.")
        sys.exit(1)

def process(input_file, output_file):
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames

        # Check if headers exist
        if headers is None or len(headers) < 1:
            print("Invalid CSV file format.")
            sys.exit(1)

        # Update headers for the new CSV (only "first" and "last")
        updated_headers = ["first", "last", "house"]

        # Prepare the new table with updated row"
        updated_rows = []
        for row in reader:
            # Split the name column into first and last name
            house = row[headers[1]]
            full = row[headers[0]].strip()  # Ensure no leading/trailing spaces
            if "," in full:
                last, first = [part.strip() for part in full.split(",", 1)]
            else:
                first, last = full, ""  # Handle cases without a comma

            # Create a new row with only first and last name
            new_row = {"first": first, "last": last, "house": house}
            updated_rows.append(new_row)

    # Write the updated rows to the new CSV file
    with open(output_file, "w", newline="") as new_csvfile:
        writer = csv.DictWriter(new_csvfile, fieldnames=updated_headers)
        writer.writeheader()
        writer.writerows(updated_rows)

if __name__ == "__main__":
    main()
