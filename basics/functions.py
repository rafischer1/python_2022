# Functions
# paramaters define what arguments a function needs
def print_message(msg="hi") -> None:
    if not isinstance(msg, str):
        print("Error: input must be string. Input type: ", type(msg))
    else:
        print(msg)


print_message("3")  # standard
print_message(msg="ok")  # defined arguments
print_message()  # uses default param
