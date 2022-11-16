from functools import reduce
# Pure Functions - same input always same output without side effects

# Q: does that include having print() in the def?


def multiply_by_two(li: list):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


def multiply_by_2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


x = multiply_by_two([3, 4])
print(multiply_by_two([1, 2]), x)

print(list(map(multiply_by_2, [4, 5, 6])))
print(list(filter(only_odd, [4, 5, 6, 7])))


# reduce
def accumulator(acc, item):
    return acc * item


print(reduce(accumulator, [4, 5, 6, 7], 20))

# lambda expressions
# one time anon funcs [you only use once!]

print(list(map(lambda item: item * 100, [4, 5, 6])))
print(reduce(lambda acc, item: acc + item, [4, 5, 6, 7], 20))

# comprehensions on list, set, dict

my_list_comp = [i for i in 'hello' if i == "l"]
print(my_list_comp)

fizz_buzz = ['fizz_buzz' if i % 3 == 0 and i % 5 == 0 else 'fizz' if i %
            3 == 0 else 'buzz' if i % 5 == 0 else i for i in range(1, 51)]

print(fizz_buzz)
