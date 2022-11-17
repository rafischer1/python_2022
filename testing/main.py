please_enter_number = "Please enter number"


def do_something(num):
    try:
        if num:
            return num + 5
        else:
            return please_enter_number
    except TypeError as err:
        return err
