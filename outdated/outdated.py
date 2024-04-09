def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ")

            if '/' in date:
                mm, dd, aa = date.strip().split('/')
                mm, dd = int(mm), int(dd)
                if mm > 12 or dd > 31:
                    pass
                else:
                    print(f"{aa}-{mm:02}-{dd:02}")
                    break
            elif ',' in date:
                mm, dd, aa = date.split()
                dd = int(dd.strip(','))
                if dd > 31:
                    pass
                else:
                    print(f"{aa}-{(months.index(mm)+1):02}-{dd:02}")
                    break
            else:
                pass

        except (KeyError, ValueError):
            pass


main()
