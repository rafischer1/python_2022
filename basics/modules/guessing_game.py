from random import randint
import sys
from color_tools import colored, cprint

lower = int(sys.argv[1])
upper = int(sys.argv[2])
answer = randint(lower, upper)


while True:
    try:
        guess = input(f'Pick a number from {lower} to {upper}: ')
        if lower <= int(guess) <= upper:
            if int(guess) == answer:
                text = colored(f" {guess}...nailed it! ", 'green',
                               attrs=['reverse', 'blink'])
                cprint(text)
                break
        else:
            text = colored(f" Hey! {lower} to {upper} pleeeze. ", 'red',
                           attrs=['reverse', 'blink'])
            cprint(text)
    except ValueError:
        print("Please try again (with a number!)")
        continue
