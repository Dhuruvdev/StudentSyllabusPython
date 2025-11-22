# Program 4: Create a binary file with names and roll numbers, then search for a roll number

import pickle

def create_file():
    file = open("Sample_Data/students.dat", "wb")
    students = [
        {"name": "Rahul", "roll": 101},
        {"name": "Priya", "roll": 102},
        {"name": "Amit", "roll": 103},
        {"name": "Neha", "roll": 104}
    ]
    pickle.dump(students, file)
    file.close()
    print("Binary file created successfully!")

def search_roll():
    roll_no = int(input("Enter roll number to search: "))
    file = open("Sample_Data/students.dat", "rb")
    students = pickle.load(file)
    file.close()
    
    found = False
    for student in students:
        if student["roll"] == roll_no:
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            found = True
            break
    
    if not found:
        print("Roll number not found!")

create_file()
search_roll()
