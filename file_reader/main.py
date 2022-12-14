# my_file = open("test.txt")  # returns a file object once TextIOWrapper
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

try:
    with open("test.txt", mode='r+') as my_file:
        text = my_file.write("😀")
        print(f"{my_file.readlines()} is the thing on this page.")
except FileNotFoundError as err:
    print("Error: File not found")
    raise err
except IOError as err:
    print("Error: IO Error")
    raise err
