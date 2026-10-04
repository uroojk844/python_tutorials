fruits = []

fruits.append("mango")
fruits.append("banana")
fruits.append("apple")

fruits.insert(0, "apple")

print("Fruit at index 0", fruits[0])

print(fruits)

print("Apple count", fruits.count("apple"))


# print("before",fruits)

# fruits.pop()
# fruits.pop(1)

# del fruits[0]

# print("After",fruits)

fruits.remove("apple")
print(fruits)

fruits.sort()
print("After sort", fruits)

fruits.append("kiwi")
fruits.sort(key=len)
print("After sort by len", fruits)

fruits.extend(["grapes", "orange"])
print("Fruits", fruits)

fruits1 = fruits.copy()
print("Fruits1", fruits1)

fruits.clear()

print(fruits, fruits1)