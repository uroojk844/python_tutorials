students = dict()


def details(text: str, width: int = 60):
    print("=" * width)
    print(text)
    print("=" * width)


while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Find student")
    print("4. Exit")
    option = int(input("Select any option: "))

    match option:
        case 1:
            name = input("Enter name: ")
            klass = input("Enter class: ")
            roll = len(students) + 1

            student = {
                "name": name,
                "clas": klass,
                "roll": roll,
            }

            students.update({roll: student})

            details(f"Student Details: {student}")
        case 2:
            details(f"School: {students}", width=120)
        case 3:
            roll = int(input("Enter roll: "))

            student = students.get(roll)
            details(f"Student Details: {student}")
        case 4:
            exit(0)
