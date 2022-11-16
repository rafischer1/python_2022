# Pure Functions - same input always same output without side effects

# Q: does that include having print() in the def?

def multiply_by_two(li: list):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


def multiply_by_2(item):
    return item * 2


x = multiply_by_two([3, 4])
print(multiply_by_two([1, 2]), x)

print(list(map(multiply_by_2, [4, 5, 6])))
