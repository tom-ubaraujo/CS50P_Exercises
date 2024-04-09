def convert(phrase):
    phrase = phrase.replace(':)', '🙂')
    phrase = phrase.replace(':(', '🙁')
    return phrase

def main():
    converted_phrase = convert(input("Insert a phrase here: "))
    print(converted_phrase)

main()