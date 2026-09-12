students = {
    "student1": {
        "name": "Kunal",
        "age": 35,
        "course": "Python"
    },
    "student2": {
        "name": "Rahul",
        "age": 30,
        "course": "SQL"
    }
}

print("All students:", students)

print("Student 1 name:", students["student1"]["name"])
print("Student 1 course:", students["student1"]["course"])

print("Student 2 name:", students["student2"]["name"])

students["student1"]["skill"] = "Machine Learning"

print("Updated Student 1:", students["student1"])