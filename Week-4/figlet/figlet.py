import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

def input_print():
    text = input("Input: ")
    print(f"Output: {figlet.renderText(text)}")

def main():

    if ind_random == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in fonts):
            figlet.setFont(font = sys.argv[2])
            input_print()
        else:
            sys.exit("Invalid usage")
    elif ind_random == 1:
        font = random.choice(fonts)
        figlet.setFont(font = font)
        input_print()
    else:
        sys.exit("Invalid usage")

if (len(sys.argv) == 1) or (len(sys.argv) == 3):
    ind_random = len(sys.argv)
    main()
else:
    sys.exit("Invalid usage")