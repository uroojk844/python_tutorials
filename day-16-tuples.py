# tuple : collection of items, unchangeable
fruits = tuple(("apple", "banana"))

f1 = [*fruits]
f1.append("mango")

fruits = tuple(f1)

print(fruits)

# for f in fruits:
#     print(f)
