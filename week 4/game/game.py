import random

# Solicita o nível ao usuário
while True:
    try:
        x = int(input("Level: "))
        if x > 0:  # O nível deve ser maior que zero
            break
    except ValueError:
        pass  

y = random.randint(1, x)

while True:
    try:
        z = int(input("Guess: "))
        if z < y:
            print("Too small!")
        elif z > y:
            print("Too large!")
        else:
            print("Just right!")
            break  # Sai do loop quando o usuário acerta
    except ValueError:
        pass
