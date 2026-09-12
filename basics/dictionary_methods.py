student = {
    "name": "Kunal",
    "age": 35,
    "course": "Python",
    "city": "Nagpur"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))
print("Country:", student.get("country", "Not available"))

student.update({"age": 36, "skill": "SQL"})
print("After update:", student)

removed_value = student.pop("city")
print("Removed city:", removed_value)
print("After pop:", student)

student.clear()
print("After clear:", student)