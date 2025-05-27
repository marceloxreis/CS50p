import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):  # 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        tries = 0
        while tries < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1

        if tries == 3:  # Show correct answer after 3 failed attempts
            print(f"{x} + {y} = {correct_answer}")

    # Only output the final score
    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)  # 1-digit number
    elif level == 2:
        return random.randint(10, 99)  # 2-digit number
    elif level == 3:
        return random.randint(100, 999)  # 3-digit number
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
