import re 
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search("(.*)\/embed\/(.+)\"",s):
        id_video = match.group(2)
        return f"https://youtu.be/{id_video}"
    return None

if __name__ == "__main__":
    main()