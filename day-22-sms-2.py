school = dict()

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

            students: list[dict] = school.get(klass, [])

            student = {
                "name": name,
                "clas": klass,
                "roll": len(students) + 1,
            }

            students.append(student)

            school.update({klass: students})

            print("=" * 60)
            print(f"Student Details: {student}")
            print("=" * 60)
        case 2:
            print("=" * 120)
            print(f"School: {school}")
            print("=" * 120)
        case 3:
            klass = input("Enter class: ")
            roll = input("Enter roll: ")

            klass_students: list[dict] = school.get(klass, [])

            for s in klass_students:
                if s.get("roll") == roll:
                    print(f"Student: {s}")
        case 4:
            exit(0)
