student = {
    "name": "Kunal",
    "age": 35,
    "course": "Python",
    "city": "Nagpur"
}

print("Student:", student)

print("Name:", student["name"])
print("Age:", student["age"])

student["age"] = 36
print("Updated age:", student["age"])

student["skill"] = "SQL"
print("After adding skill:", student)

student.pop("city")
print("After removing city:", student)

print("Keys:", student.keys())
print("Values:", student.values())