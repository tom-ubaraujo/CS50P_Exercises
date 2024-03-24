def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s.isalnum():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for idx in range(len(s)):
        if s[idx].isdecimal():
            if s[idx] != '0' and s[idx:].isdecimal():
                return True
            else:
                return False

    return True

main()