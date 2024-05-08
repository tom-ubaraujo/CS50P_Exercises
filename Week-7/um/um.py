import re

def main():
    print(count(input("Text: ")))

def count(s):
    list_phrase = re.findall(r"\b\W*um\W*\b", s, re.IGNORECASE)
    return len(list_phrase)

if __name__ == "__main__":
    main()