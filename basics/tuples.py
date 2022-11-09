# Tuple
# immutable list of items
# easier and efficient unmodifiable list but you can't sort | reverse | etc but perform faster

my_tuple = (1, 2, 3, 4, 1)
print(4 in my_tuple, my_tuple)

# dict method .items() returns items in a tuple

x, y, *other = my_tuple
print(other, x, y)
print(my_tuple.count(1), len(my_tuple))

# two methods: count() and index()
