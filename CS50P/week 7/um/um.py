import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(match)  # Retorna o número real de ocorrências


if __name__ == "__main__":
    main()
