class Person:
    def __init__(self, name, dob) -> None:
        self.name = name
        self.dob = dob

    def __str__(self) -> str:
        return self.name + " " + str(self.dob)


p1 = Person("John Doe", 1995)
print(p1)


class Student(Person):
    def __init__(self, name, dob, roll) -> None:
        super().__init__(name, dob)
        self.roll = roll

    def get_roll(self):
        return self.roll


s1 = Student("Raj", "2000", 1)
print(s1)
s1.roll = 10
print(s1.roll)
