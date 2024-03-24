import emoji

def main():
    text = input()
    print(emoji.emojize(f"Output: {text}", language="alias"))



main()