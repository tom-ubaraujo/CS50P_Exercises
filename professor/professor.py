import random


def main():
    game_level = get_level()
    correct = 0

    for i in range (10):
        x , y = generate_integer(game_level)
        tries = 0

        while tries < 3:

            try:
                answer = int(input(f"{str(x)} + {str(y)} = "))
                if answer == x + y:
                    correct += 1
                    break
                else:
                    raise ValueError

            except:
                tries += 1
                print("EEE")
                if tries == 3:
                    print(f"{str(x)} + {str(y)} = {x+y}")
                pass

    print(f"Score: {correct}")


def get_level():
    while True:
        level = input("Level: ")
        if level != "1" and level != "2" and level != "3":
            continue
        else:
            return int(level)


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()