# Higher Order Functions and Decorators
# accept a func as param or returns a func


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("......")
        func(*args, **kwargs)
        print("*******")
    return wrap_func


@my_decorator
def hello(msg, emoji="🚛"):
    print(msg + " " + emoji)


hello("hi")
# or...

# hello2 = my_decorator(hello)
# hello2()
