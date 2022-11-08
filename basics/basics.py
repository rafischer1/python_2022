# interpreter runs line -> byte code -> cpythonVM
print("Cool Dude")
x = input("Having fun yet? ")
print(x)
if isinstance(x, str):
    print("Best Answer!: " + x)

# can do multiple assignments
a, b, c = 1, 2, 3
print(a, c, b)
