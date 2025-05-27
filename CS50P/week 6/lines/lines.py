import sys
import os


def main():
    # Check command-line arguments and file validity
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file_name = sys.argv[1]
    check(file_name)
    line_count(file_name)


def check(file_name):
    # Check if the file has a .py extension
    if not file_name.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    # Check if the file exists
    if not os.path.exists(file_name):
        print("File does not exist.")
        sys.exit(1)

def line_count(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            stripped = line.strip()
            # Skip blank lines and comments
            if stripped == "" or stripped.startswith("#"):
                continue
            else:
                count += 1
    print(count)





if __name__ == "__main__":
    main()
