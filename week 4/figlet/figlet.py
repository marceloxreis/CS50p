from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    font = sys.argv[2]
    if font not in figlet.getFonts():
        print("Invalid font")
        sys.exit(1)
    text = input("Input: ")
    figlet.setFont(font=font)
    print(figlet.renderText(text))
else:
    sys.exit(1)
