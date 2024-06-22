import re
import random
import sys

args = sys.argv[1:]

def main():
    CMD, SERVICE = validate_input(args)

    if CMD == 'r':
        print(read_pass(SERVICE))
    elif CMD == 'w':
        mail, service, size = get_info()
        write_file(service, mail, gen_password(size))
    else:
        print("Invalid Command!"); sys.exit(1)

def validate_input(args):
    if not args:
        print("Must inform at least one command('r' or 'w')"); sys.exit(1)
    elif len(args) > 2:
        print("Too many comands informed"); sys.exit(1)
    elif len(args) == 2:
        return args[0].lower(), args[1].lower()
    else:
        return args[0], None

def get_info():
    print("WELCOME - GENERATE AND KEEP RECORD OF PASSWORDS")
    email = input("Inform the email used with the password: ")
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        print("Invalid email"); sys.exit(1)
    service = input("Inform the service of the password: ")
    if len(service) < 1:
        print("Invalid service"); sys.exit(1)
    size = int(input("Inform the size of password between 8 and 32: "))
    if size < 8 or size > 32:
        print("Invalid size for the password"); sys.exit(1)
    return email, service, size

def gen_password(size=8):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<'] 
    all_chars = digits + lower + upper + special
    password = ""
    for i in range(size):
        password += random.choice(all_chars)
    password = list(password)
    random.shuffle(password)
    return "".join(password)

def write_file(service, email, password):
    with open("note_pass.txt", "a") as file_:
        file_.write(f"{service};{email};{password}\n")
        print("Password generated: ")
        print(f"Service: {service}\nEmail: {email}\nPassword: {password}\n")

def read_pass(svc=None):
    print("* --- PASSWORD NOTEPAD --- *\n")
    text = ""
    if svc:
        for linha in open("note_pass.txt", "r"):
            service, mail, password = linha.split(';')
            if svc == service.lower():
                text = f"Service: {service}\nEmail: {mail}\nPassword: {password}\n" + "* --- * --- * --- * --- * --- *\n"
    else:
        for linha in open("note_pass.txt", "r"):
            service, mail, password = linha.split(';')
            text += f"Service: {service}\nEmail: {mail}\nPassword: {password}\n" + "* --- * --- * --- * --- * --- *\n"
    return text

if __name__ == "__main__":
    main()