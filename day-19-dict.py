student = {
    "name": "John",
    "age": "21",
    "class": "10",
    "subjects": ["english", "math", "science"],
}


print(student["name"])
print(student["age"])


print(student["subjects"])
print(student.get("subject", "Not exist"))


# student["school"] = "Delhi University"
student.update({"school": "Delhi University"})
# print(student["school"])

print(student)
