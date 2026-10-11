class Shape:
    def __init__(self, name: str) -> None:
        self.name = name
        self.values()

    def values(self):
        values = input(f"Enter side(s) of {self.name} separated by spaces: ")
        values = values.split(" ")
        self.intValues = list(map(int, values))
        return self.intValues


class Square(Shape):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def area(self):
        if len(self.intValues) > 0:
            print("Area of square is", self.intValues[0] ** 2)


class Rectangle(Shape):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def area(self):
        if len(self.intValues) > 0:
            print("Area of rectangle is", self.intValues[0] * self.intValues[1])


s = Square("square")
s.area()

r = Rectangle("rectangle")
r.area()
