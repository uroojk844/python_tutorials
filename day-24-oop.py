class Car:
    type = "SUV"

    def __init__(self, brand: str, name: str) -> None:
        self.brand = brand
        self.name = name

    def detail(self):
        print(f"Car type is {self.type}")
        print(f"Brand: {self.brand}")
        print(f"Name: {self.name}")


car1 = Car("bmw", "m4")

car1.detail()
