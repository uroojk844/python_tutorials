print("1. Add Student")
print("2. Show Students")
print("3. Find student")
print("4. Exit")
option = int(input("Select any option: "))

school = dict()

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

        print(school)
    case 4:
        exit(0)
