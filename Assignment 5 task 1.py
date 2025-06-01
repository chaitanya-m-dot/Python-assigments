dictionary = {'alice': 85, 'jacob': 40, 'carl': 55, 'ethan': 83}
name = input("Enter the student's name: ").lower()

if name in dictionary:
    print(f"{name}'s marks : {dictionary[name]}")
else:
    print("Student not found.")
