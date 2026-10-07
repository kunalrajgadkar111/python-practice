numbers = [10, 20, 30, 40, 50]
print(30 in numbers)  # True
print(60 in numbers)  # False
print(30 not in numbers)  # False
print(60 not in numbers)  # True


# whether python is in the list of programming languages
programming_languages = ["Python", "Java", "C++", "JavaScript"]    
print("Python" in programming_languages)  # True
print("Ruby" in programming_languages)  # False 
print("Python" not in programming_languages)  # False
print("Ruby" not in programming_languages)  # True  

# data = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# Check whether:
# [40, 50, 60]
# # is present in data. *

data = [
     [10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
 ]
print([40, 50, 60] in data)  # True

result = [40, 50, 60] in data
print(result)

result = 40 in data
print(result)