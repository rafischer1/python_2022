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
