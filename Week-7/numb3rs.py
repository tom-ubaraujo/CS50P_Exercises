import re

def main():
    print(validate(input("IPv4 address: ").strip()))

def validate(ip):
    match =  re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)

    if match:
        for i in range(1,5):
            if int(match.group(i)) > 255 or int(match.group(i)) < 0:
                return False
        return True
    return False

if __name__ == '__main__':
    main()