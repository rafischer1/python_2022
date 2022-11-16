# For Loops
import asyncio
my_list = ["a", "b", "c"]

for i in my_list:
    print(i, my_list.index(i))


user = {"name": "Golem", "age": 543, "can_swim": False}

# for i in user:
#     print({i: user[i]})

# for i in user.items():
#     for x in user.values():
#         print(i, x)

for key, value in user.items():
    print(key, value)

# range()
for i in range(0, 20, 3):
    if i % 5 == 0:
        print(i)

# enumerated - for needing index counter
for i, char in enumerate("hi"):
    print(i, char)

# while - not sure how long a loop will take or it needs a condition
i = 2
while 0 < 5 and i != 0:
    print(i)
    i = i - 1

while True:
    response = input("Say something: ")
    break

# continue goes back to the loop
# pass does nothing - useful for a placeholder

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print("")  # prints new line after every row

# check duplicates
some_list = ["a", "b", "c", "b", "m", "n", "n"]
duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

print(duplicates)
# Quick async hookup with asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(.5)
    print('... World!')

asyncio.run(main())
