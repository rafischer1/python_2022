# Sets
# unordered collections of unique objects
my_set = {1, 2, 3, 4, 5, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
# no duplicates!
my_set.add(6)
print(my_set)

# remove all duplicates from a list to set set(my_list)
print(1 in my_set, len(my_set))

# .difference()
print(my_set.difference(your_set), your_set.difference(my_set))

# intersection (what is in common) or &
print(my_set.intersection(your_set), my_set & your_set)
# isdisjoint (do they have nothing in common)
print(my_set.isdisjoint(your_set))
# .union() || |
print(my_set | your_set)

# issubset() the first set is entirely inside of other set
# is superset the first set encompasses the other set
