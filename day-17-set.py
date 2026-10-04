# Set - {}

numbers = {0, 1, 2, 3, 4, 1, 4, 2, 5, True, False}

print("Before", numbers)

# for num in numbers:
#     if num == 2:
#         print("skipping 2")
#     else:
#         print(num)

# print(10 in numbers)

numbers.add(6)

numbers.update([10, 11, 123])
numbers.update((10, 11, 123))
numbers.update({10, 11, 123})

last =  numbers.pop()
last =  numbers.pop()

del numbers

print(last)

# print("After", numbers

