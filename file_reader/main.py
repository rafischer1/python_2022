# my_file = open("test.txt")  # returns a file object once TextIOWrapper
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

with open("test.txt", mode='r+') as my_file:
    text = my_file.write("😀")
    print(my_file.readlines())
