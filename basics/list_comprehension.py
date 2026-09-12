# Basic list comprehension

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Numbers:", numbers)
print("Squares:", squares)


# With condition

even_numbers = [x for x in numbers if x % 2 == 0]

print("Even numbers:", even_numbers)


# Transforming strings

names = ["kunal", "rahul", "aniket"]

uppercase_names = [name.upper() for name in names]

print("Names:", names)
print("Uppercase:", uppercase_names)


# Condition + transformation

marks = [45, 67, 32, 89, 56]

passed_marks = [mark for mark in marks if mark >= 40]

print("Marks:", marks)
print("Passed:", passed_marks)