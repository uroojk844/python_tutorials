def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    def decrease():
        nonlocal count
        count -= 1
        return count

    return increase, decrease


increase, decrease = counter()

print(increase())
print(increase())
print(increase())

print(decrease())
print(decrease())
