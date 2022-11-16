# OOP - everything is built with <class ...>

# creating custom objects with the class keyword

class BigObject:  # Class
    pass


obj1 = BigObject()  # instantiate

# print(type(obj1))


class Character:
    logged_in = True  # class object attribute

    def __init__(self, name):
        if self.logged_in:
            self.name = name

    def move_forward(self):
        return f'{self.name} ->'

    def move_backward(self):
        return f'{self.name} <-'

    @classmethod
    def return_to_start(cls):
        return f'{cls.name} at start.'

    @staticmethod
    def game_over():
        return "Game Over"


c1 = Character(name="Me")
c2 = Character("You")
print(c1.move_forward())
print(c2.move_backward())
