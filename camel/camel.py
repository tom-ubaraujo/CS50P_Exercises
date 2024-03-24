camel_case = input("camelCase: ")

snake_case = []

for letter in camel_case:
    if letter.isupper():
        snake_case.append("_")
        snake_case.append(letter.lower())
    else:
        snake_case.append(letter)

print("".join(snake_case))