# Errors

while True:
    try:
        age = int(input("how many years do you have? "))
        print(age)
    except ValueError as err:
        print(f"Bad input!!! Try age in years. [err: {err}]")
    else:
        print("Years and Years")
        break
