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
            res.append(str(i) + ": FIZZ BUZZ (3 & 5)")
        elif i % 3 == 0 and i % 5 != 0:
            res.append(str(i) + ": FIZZ (3)")
        elif i % 5 == 0 and i % 3 != 0:
            res.append(str(i) + ": BUZZ (5)")
    return res


fizz = fizz_buzz(100)
# print(fizz)

# methods exist on the type
print("hi".capitalize())

# docstrings


def test(a):
    '''
    Info: this func prints param A
    '''
    print(a, test.__doc__)


test("a")

# kwargs (key word args)


def super_func(*args, **kwargs):
    total = 0
    for i in kwargs.values():
        total += i

    return sum(args) + total


print(super_func(1, 2, 3, num=2, num2=3, num3=100))

# rule: params, *args, default params, **kwargs


def highest_even(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)


print("HIGHEST EVEN: ", highest_even([11, 12, 1, 2, 3, 4]))

# walrus operator :=
walrus = "walrussdaffsdf"
if ((n := len(walrus)) > 10):
    print(f"too long a walrus {n}")
