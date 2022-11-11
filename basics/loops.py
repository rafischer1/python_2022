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
for i,char in enumerate("hi"):
  print(i, char)



# Quick async hookup with asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(.5)
    print('... World!')

asyncio.run(main())
