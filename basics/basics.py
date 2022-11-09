# interpreter runs line -> byte code -> cpythonVM
print("Cool Dude")
x = input("Having fun yet? ")
print(x)
if isinstance(x, str):
    print("Best Answer!: " + x)

# can do multiple assignments
a, b, c = 1, 2, 3
print(a, c, b)

# d = -1

# if d < 0:
#     raise Exception("Sorry, no numbers below zero")

# augmented assignment operator
some_value = 5
some_value += 2
print(some_value)

# escape sequences
weather = 'It\'s \t sunny \n now'
print(weather)
