def main():

    hour = convert(input("What time is it? "))

    if hour >= 7 and hour <= 8:
        print("breakfast time")
    elif hour >= 12 and hour <= 13:
        print("lunch time")
    elif hour >= 18 and hour <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours)


if __name__ == "__main__":
    main()