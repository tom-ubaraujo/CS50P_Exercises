def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if not plate.isalnum():
        return False

    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    for idx in range(len(plate)):
        if plate[idx].isdecimal():
            if plate[idx] != '0' and plate[idx:].isdecimal():
                return True
            else:
                return False

    return True

main()