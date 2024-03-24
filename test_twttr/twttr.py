def main():

    text = input("Input: ")
    print(shorten(text))


def shorten(text):

    vowels = ['a','e','i','o','u','A','E','I','O','U']
    txt = []

    for letter in text:
        if letter in vowels:
            pass
        else:
            txt.append(letter)

    return "".join(txt)


if __name__ == "__main__":
    main()