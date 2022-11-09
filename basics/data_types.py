# Data Types

# Fundamental Types

# int <class 'int'>
print(type(2 + 4))
print(2 ** 4)
print(5 // 4)
print(6 % 4)
# float <class 'float'>
print(type(2 / 4))
print(bin(5), int("0b101", 2))  # can print binary number
# complex (barely used)

# math functions
print(round(3.5))
print(abs(-3.5))
# bool <class 'bool'>
print(type(2 == 2))
# str <class 'str'>
long_string = '''
WOW
00
----
.........
MOM
'''
print(type("2"), long_string)

# type conversion
print(type(int(str(100))))

# formatted string
name = "Artman"
age = 33
print(f"Hi {name} you are {age + 6} years old")
print("Hi {1} you are {0} years old".format("Dude", age))
print("Hi {new_name} you are {new_age} years old".format(
    new_name="Cool", new_age=4))
print(name[1:6:2])  # start:stop:stepover
print(name[::-1])  # reverse a string
# list
# tuple
# set
# dict

# Classes -> custom types

# Specialized Types (classes and modules from libraries)

# The absence of value -> None
None

# operators
# + - / * **

# operator precedence
print((20 - 3) + 2 ** 2)
# ()
# ** power of
# * /
# + -
