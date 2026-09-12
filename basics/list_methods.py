fruits = ["apple", "banana", "mango"]

fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "grapes")
print("After insert:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

removed_fruit = fruits.pop()
print("Popped fruit:", removed_fruit)
print("After pop:", fruits)

fruits.sort()
print("Sorted:", fruits)

fruits.reverse()
print("Reversed:", fruits)

print("Count of mango:", fruits.count("mango"))
print("Index of mango:", fruits.index("mango"))