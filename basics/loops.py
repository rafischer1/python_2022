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

# Quick async hookup with asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(.5)
    print('... World!')

asyncio.run(main())
