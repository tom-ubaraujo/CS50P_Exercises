# how to discover the percentage:
# 3/4 -> 100 / 4 = 25 -> 25 * 3 = 75%
# x/y -> 100 / y = 25 -> 25 * x = 75%
# 3/5 -> 100 / 5 = 20 -> 20 * 3 = 60%

def main():
    f = input("F: ")
    remain_fuel = gauge(convert(f))
    print(remain_fuel)

def convert(f):
    while True:
        try:
            x , y = f.split("/")
            x , y = int(x), int(y)
            value = x / y
            if value <= 1:
                return int(value * 100)
            else:
                f = input("F: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(n):
    if n <= 1:
        return "E"
    elif n >= 99:
        return "F"
    else:
        return f"{n}%"

if __name__ == "__main__":
    main()