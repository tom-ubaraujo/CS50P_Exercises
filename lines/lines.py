import sys

arguments = sys.argv[1:]

def count_lines(file):
    count = 0
    try:
        for line in open(file, "r"):

            line = line.lstrip()

            if len(line.lstrip()) > 1:
                if line.startswith("# "):
                    pass
                else:
                    count += 1
            else:
                pass
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    
    return count

if not arguments:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(arguments) > 1:
    print("Too many command-line arguments")
    sys.exit(1)
elif not arguments[0].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)
else:
    print(count_lines(arguments[0]))