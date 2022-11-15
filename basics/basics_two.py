# Conditional Logic
is_old = True
is_licensed = True

if is_old and is_licensed:
    print("Old enough and licensed!")
elif not is_licensed & is_old:
    print("No license")
else:
    print("No way")

# Ternary operator
is_friend = False
is_user = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting 'or' 'and'
print(is_friend or is_user, is_user and is_friend)
# short circuits if the first condition is met

# Logical Operators
# and or > < == != not
print("a" > "A")  # True -> ascii numbering 97 > 65
print(not (1 == 1))  # Flips the script

# is vs ==
print(True == 1)  # bool(1) so true
print(True is 1)
print(1 is 1)  # is the location in memory the same
print([] is [])  # False because lists are created in new locations

# SCOPE in python
# 1. start with local var
# 2. Parent local?
# 3. Global var
# 4. built in python functions

# nonlocal refers to # 2


def outer():
    x = "local"

    def inner():
        nonlocal x  # redefine that outer scope x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)


outer()
