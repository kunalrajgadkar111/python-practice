# Normal function

def square(x):
    return x * x

print("Normal function:", square(5))


# Lambda function

square_lambda = lambda x: x * x

print("Lambda function:", square_lambda(5))


# Addition

add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Check even or odd

is_even = lambda x: x % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))


# Lambda with a list

numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers, key=lambda x: x)

print("Original:", numbers)
print("Sorted:", sorted_numbers)


# Sorting names by length

names = ["Kunal", "Rahul", "Aniket", "Himanshu"]

sorted_names = sorted(names, key=lambda name: len(name))

print("Names:", names)
print("Sorted by length:", sorted_names)