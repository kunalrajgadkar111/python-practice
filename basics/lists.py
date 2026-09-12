fruits = ["apple", "banana", "mango", "orange"]

print("Fruits:", fruits)

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

print("First two fruits:", fruits[0:2])

fruits.append("grapes")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

print("Number of fruits:", len(fruits))