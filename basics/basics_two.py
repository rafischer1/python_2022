# Conditional Logic
is_old = True
is_licensed = False

if is_old and is_licensed:
    print("Old enough and licensed!")
elif not is_licensed & is_old:
    print("No license")
else:
    print("No way")
