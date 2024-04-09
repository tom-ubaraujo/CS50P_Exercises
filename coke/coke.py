owed = 50

print("Amount due: ", owed)

while owed > 0:

    coin = int(input("Insert Coin: "))
    match coin:
        case 5 | 10 | 25:
            owed -= coin
        case _:
            pass

    if owed > 0:
        print("Amount due: ", owed)
    else:
        print("Change owed: ", owed * -1)