import sys
import os
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    file_name = sys.argv[1]
    check(file_name)
    price(file_name)

def check(file_name):
    if not file_name.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)

    if not os.path.exists(file_name):
        print("File does not exist.")
        sys.exit(1)

def price(file_name):
    table = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)  # Reads each row as a dictionary
        # Dynamically get the pizza column name (first column)
        headers = reader.fieldnames  # Get the list of column names

        pizza_column = headers[0]
        small_column = headers[1]
        large_column = headers[2]

        for row in reader:
            try:
                pizza_name = row[pizza_column]
                small_price = row[small_column]
                large_price = row[large_column]
                table.append([pizza_name, small_price, large_price])
            except ValueError :
                pass
    if table:  # Ensure the table isn't empty before printing
        print(tabulate(table, headers=[headers[0], "Small", "Large"], tablefmt="grid"))


if __name__ == "__main__":
    main()
