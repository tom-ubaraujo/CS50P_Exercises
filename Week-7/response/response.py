from validator_collection import validators

def main():
    print(email_validation(input("What's your email address? ")))
    
def email_validation(mail):
    try:
        if validators.email(mail):
            return "Valid"
    except:
        return "Invalid"

if __name__ == "__main__":
    main()