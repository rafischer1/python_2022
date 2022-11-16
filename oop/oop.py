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
            self._name = name

    def move_forward(self):
        return f'{self._name} ->'

    def move_backward(self):
        return f'{self._name} <-'

    @classmethod
    def return_to_start(cls):
        return f'{cls._name} at start.'

    @staticmethod
    def game_over():
        return "Game Over"

    def __call__(self):
        print("Is it me you're looking for???")


c1 = Character(name="Me")
c2 = Character("You")
print(c1.move_forward())
print(c2.move_backward())


def move_char_forward(char: Character):
    print(char.move_forward())


c2()
move_char_forward(c2)


"""
Encapsulation: data, methods, attributes encompassed by the Object class

Abstraction: only access what is necessary (c1.move_forward()) is all the info needed to make the action happen

Inheritance: class Wizard(Character) -> new sub class inherits passed parent class

Polymorphism: classes can share method names see def move_char_forward()

GOTCHA: python does allow multiple inheritance
check with .mro()
"""

# print(help(c1))
print(Character.mro())
