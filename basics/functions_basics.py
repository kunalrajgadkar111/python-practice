# Basic function

def greet():
    print("Hello, Kunal!")


greet()


# Function with a parameter

def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Kunal")
greet_person("Rahul")


# Function with multiple parameters

def add_numbers(a, b):
    print(f"Sum: {a + b}")


add_numbers(10, 20)
add_numbers(50, 25)


# Function that returns a value

def multiply(a, b):
    return a * b


result = multiply(5, 6)

print("Multiplication:", result)