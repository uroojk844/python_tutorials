class1 = ["John", "Sam", "Foo"]

print("1. Show all students")
print("2. Show students by index")
print("3. Add student")
print("4. Exit")

def performAction():
    option = int(input("Select option: "))

    match option:
        case 1:
            print(f"\nAll Students of class 1\n{class1}\n")
        case 2:
            index = int(input(f"Enter index (0 - {len(class1) - 1}): "))
            print(f"\nStudent at {index}\nName: {class1[index]}\n")
        case 3:
            name = input(f"Enter name: ")
            class1.append(name)

            print(f"{name} is added at index {len(class1)-1}")
        case 4:
            exit(0)

performAction()
performAction()