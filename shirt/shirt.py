import sys
from PIL import Image, ImageOps

arguments = sys.argv[1:]

type_in, type_out = arguments[0].split('.')[1].lower(), arguments[1].split('.')[1].lower()
valid_fomats = ('jpg', 'jpeg', 'png')

def valid_input():
    if len(arguments) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(arguments) < 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif type_in not in valid_fomats:
        print("Invalid input")
        sys.exit(1)
    elif type_out not in valid_fomats:
        print("Invalid output")
        sys.exit(1)
    elif type_in != type_out:
        print("Input and output have different extensions")
        sys.exit(1)
    return True


def main():
    if valid_input():
        try:
            shirt = Image.open('shirt.png')
            before = Image.open(arguments[0])
            before = ImageOps.fit(before, (600,600))
            before.paste(shirt, shirt)
            before.save(arguments[1])
        except FileNotFoundError:
            print("Input does not exist")
            sys.exit(1)

if __name__ == '__main__':
    main()