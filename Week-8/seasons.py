from datetime import date
import sys
import inflect

def main():
    print(gen_text(get_date()))

def get_date():
    date_in = input("Date of Birth: ")

    try:
        date_in = date_in.split("-")
        date_in = date(int(date_in[0]), int(date_in[1]), int(date_in[2]))
        today = date.today()
    except:
        print("Invalid date")
        sys.exit(1)

    days_between = today - date_in # returns a timedelta object
    total_minutes = days_between.total_seconds() / 60

    return int(total_minutes)

def gen_text(number):
    p = inflect.engine()
    numbers =  p.number_to_words(number, andword="", wantlist=True)
    numbers = ", ".join(numbers) + " minutes"
    return numbers.capitalize()

if __name__ == "__main__":
    main()