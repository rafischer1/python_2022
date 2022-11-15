# Functions
# paramaters define what arguments a function needs
def print_message(msg="hi") -> None:
    if not isinstance(msg, str):
        print("Error: input must be string. Input type: ", type(msg))
    else:
        print(msg)


print_message("3")  # standard
print_message(msg="ok")  # defined arguments
print_message()  # uses default param


def fizz_buzz(x: int) -> list:
    res = []
    for i in range(x + 1):
        if i == 0:
            pass
        elif i % 3 == 0 and i % 5 == 0:
            res.append(str(i) + " FIZZ BUZZ")
        elif i % 3 == 0 and i % 5 != 0:
            res.append(str(i) + " FIZZ")
        elif i % 5 == 0 and i % 3 != 0:
            res.append(str(i) + " BUZZ")
    return res


fizz = fizz_buzz(100)
print(fizz)
