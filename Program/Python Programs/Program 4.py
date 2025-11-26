# Program 4: Create a DAT file with student data and search by roll number

import pickle

file = open("Data/students.dat", "wb")
students = [
    {"name": "Rahul", "roll": 101},
    {"name": "Priya", "roll": 102},
    {"name": "Amit", "roll": 103}
]
pickle.dump(students, file)
file.close()

roll_no = int(input("Enter roll number to search: "))
file = open("Data/students.dat", "rb")
students = pickle.load(file)
file.close()

for student in students:
    if student["roll"] == roll_no:
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        break
