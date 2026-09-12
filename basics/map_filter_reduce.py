from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - applies a function to every item
squares = list(map(lambda x: x * x, numbers))

print("Numbers:", numbers)
print("Squares:", squares)


# filter() - keeps items that satisfy a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)


# reduce() - combines all items into one result
total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)


# Practical example
marks = [45, 67, 32, 89, 56]

passed = list(filter(lambda mark: mark >= 40, marks))
increased_marks = list(map(lambda mark: mark + 5, marks))

print("Marks:", marks)
print("Passed:", passed)
print("Marks after adding 5:", increased_marks)