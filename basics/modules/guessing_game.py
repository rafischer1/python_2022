from random import randint
import sys

lower = int(sys.argv[1])
upper = int(sys.argv[2])
answer = randint(lower, upper)


while True:
    try:
        guess = input(f'Pick a number from {lower} to {upper}: ')
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print(f"{guess}...nailed it!")
                break
        else:
            print(f"Hey! {lower} to {upper} pleeeze.")
    except ValueError:
        print("Please try again (with a number!)")
        continue
