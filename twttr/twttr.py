text = input("Input: ")

vowels = ['a','e','i','o','u','A','E','I','O','U']
txt = []

for letter in text:
    if letter in vowels:
        pass
    else:
        txt.append(letter)

print("Output: ", "".join(txt))