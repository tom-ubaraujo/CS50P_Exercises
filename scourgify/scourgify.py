# import sys
# import csv

# arguments = sys.argv[1:]

# def scourgify_file(file):
#     with open(file, 'r') as file:
#         reader = csv.DictReader(file)
#         with open(arguments[1], "w") as out_file:
#             out_file.write('first,last,house')

#             for row in reader:
#                 last, first = row['name'].split(', ') #no split, além da virgula passei o espaço pois o arquivo esta assim
#                 out_file.write(f"\n{first},{last},{row['house']}")

# if len(arguments) < 2:
#     print("Too few command-line arguments")
#     sys.exit(1)
# elif len(arguments) > 2:
#     print("Too many command-line arguments")
#     sys.exit(1)
# elif not arguments[0].endswith(".csv"):
#     print("Not a CSV file")
#     sys.exit(1)
# else:
#     try:
#         print(scourgify_file(arguments[0]))
#     except:
#         print(f"Could not read {arguments[0]}")


# ALTERNATIVA POIS A VERSAO ACIMA NAO PASSOU NO CHECK50 - DIFFS COMENTADAS
import sys
import csv

arguments = sys.argv[1:]

def scourgify_file(file):
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        with open(arguments[1], "w") as out_file:
            # fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(out_file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            # out_file.write('first,last,house')

            for row in reader:
                last, first = row['name'].split(', ') # no arquivo tem um espaço após a virgula, sujeira
                writer.writerow({'first':first, 'last':last, 'house':row['house']})
                # out_file.write(f"\n{first},{last},{row['house']}")

if len(arguments) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(arguments) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    try:
        scourgify_file(arguments[0])
    except:
        print(f"Could not read {arguments[0]}")
        sys.exit(1)