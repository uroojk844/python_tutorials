# def add(**kwargs):
#     print(kwargs.get("name"), kwargs.get("klass"))


# add(
#     name="john",
#     klass=12,
# )

# square = lambda x, y : x * y

# print(square(5, 10))


name = "John"


def setName(newName: str):
    name = newName

    def name1():
        nonlocal name
        name = "try"

    return name1


print(name)
