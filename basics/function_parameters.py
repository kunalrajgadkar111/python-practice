# Positional arguments

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Kunal", 34)


# Default argument

def greet(name="Kunal"):
    print(f"Hello, {name}!")


greet()
greet("Rahul")


# Multiple default arguments

def student_info(name, course="M.Tech", city="Nagpur"):
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"City: {city}")


student_info("Kunal")

student_info("Rahul", "B.Tech", "Pune")


# Keyword arguments

student_info(
    name="Aniket",
    city="Mumbai",
    course="B.E."
)


# Mixing positional and keyword arguments

student_info("Himanshu", city="Delhi")