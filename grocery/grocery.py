def main():
    items = {}

    while True:
        try:
            item = input().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            print(" ")
            break

    for item in sorted(items.keys()):
       print(f"{items[item]} {item}")

main()