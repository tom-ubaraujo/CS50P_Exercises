import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                pass
            else:
                secret_number = random.randint(1, level)

                while True:
                    guess = int(input("Guess: "))

                    if guess < 0:
                        continue
                    elif guess < secret_number:
                        print("Too small!")
                        continue
                    elif guess > secret_number:
                        print("Too large!")
                        continue
                    else:
                        sys.exit("Just right!")
        except EOFError:
            print("")
            break
        except ValueError:
            pass

main()