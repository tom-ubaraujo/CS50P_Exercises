import re

def main():
    print(validate(input("IPv4 address: ").strip()))

def validate(ip):
    if match :=  re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        numbers = ip.split(".")
        for i in numbers:
            if (int(i) < 0 or int(i) > 255):
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    main()