# Modules
import utility  # creates compiled version pycache
from package.shopping_cart import buy  # importing from a package
import random
import sys

if __name__ == "__main__":
    print(utility.divide(100, 10))
    print(buy("apple"))
    print(random.randint(1, 100))
    first = sys.argv[1]
    second = sys.argv[2]
    print(f"hi {first} {second}")
