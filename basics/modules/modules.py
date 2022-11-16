# Modules
import utility  # creates compiled version pycache
from package.shopping_cart import buy  # importing from a package
if __name__ == "__main__":
    print(utility.divide(100, 10))
    print(buy("apple"))
