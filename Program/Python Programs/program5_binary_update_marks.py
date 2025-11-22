# Program 5: Create a binary file with roll number, name, and marks; update marks for a given roll number

import pickle

def create_file():
    file = open("Data/marks.dat", "wb")
    records = [
        {"roll": 1, "name": "Aman", "marks": 85},
        {"roll": 2, "name": "Sonia", "marks": 90},
        {"roll": 3, "name": "Karan", "marks": 78}
    ]
    pickle.dump(records, file)
    file.close()
    print("File created with student records!")

def update_marks():
    roll_no = int(input("Enter roll number: "))
    new_marks = int(input("Enter new marks: "))
    
    file = open("Data/marks.dat", "rb")
    records = pickle.load(file)
    file.close()
    
    for record in records:
        if record["roll"] == roll_no:
            record["marks"] = new_marks
            print("Marks updated successfully!")
            break
    
    file = open("Data/marks.dat", "wb")
    pickle.dump(records, file)
    file.close()

create_file()
update_marks()
