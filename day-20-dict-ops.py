students = {
    "id": 1,
    "name": "John",
    "subjects": ["Math", "english"],
    "dob": "1/1/1999",
    "friend": "abcd",
}

# del students["friend"]
# students.pop("friend")
# students.popitem()

# students.clear()

# del students

for k,v  in students.items():
    print(k,v)
