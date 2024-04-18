import sys
from tabulate import tabulate
import csv

argument = sys.argv[1:]

def tabulate_file(file):
    table = []
    try:
        with open(file, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                table.append(row)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if not argument:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(argument) > 1:
    print("Too many command-line arguments")
    sys.exit(1)
elif not argument[0].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)
else:
    print(tabulate_file(argument[0]))