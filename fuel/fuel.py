# how to discover the percentage:
# 3/4 -> 100 / 4 = 25 -> 25 * 3 = 75%
# x/y -> 100 / y = 25 -> 25 * x = 75%
# 3/5 -> 100 / 5 = 20 -> 20 * 3 = 60%

def main():
    remain_fuel = remaining(get_fraction())

    if remain_fuel <= 1:
        print("E")
    elif remain_fuel >= 99:
        print("F")
    else:
        print(f"{remain_fuel}%")


def get_fraction():
    while True:
        try:
            x , y = input("Fraction: ").split(sep="/")
            x , y = int(x), int(y)
            if (x <= y) and (y != 0):
                return x, y
        except ValueError:
            pass

def remaining(x_y):
    x , y = x_y
    return round((100 / y) * x)

main()