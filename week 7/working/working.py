import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError", file=sys.stderr)
        sys.exit(1)

def convert(time_range):
    # Regex para capturar o formato correto (com espaços e separação por 'to')
    match = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", time_range)

    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Se minutos forem None, definir como '00'
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    # Validações de hora e minuto
    if not (1 <= int(h1) <= 12) or not (1 <= int(h2) <= 12):
        raise ValueError
    if not (0 <= m1 < 60) or not (0 <= m2 < 60):
        raise ValueError

    # Converter para 24 horas
    h1 = convert_to_24h(int(h1), p1)
    h2 = convert_to_24h(int(h2), p2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def convert_to_24h(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12

if __name__ == "__main__":
    main()
