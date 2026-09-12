age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("You can enter.")
    else:
        print("You need an ID.")
else:
    print("You are not eligible to enter.")