# Program 5: Create and update a DAT file with marks

import pickle

file = open("Data/marks.dat", "wb")
records = [
    {"roll": 1, "name": "Aman", "marks": 85},
    {"roll": 2, "name": "Sonia", "marks": 90},
    {"roll": 3, "name": "Karan", "marks": 78}
]
pickle.dump(records, file)
file.close()

roll_no = int(input("Enter roll number to update: "))
new_marks = int(input("Enter new marks: "))

file = open("Data/marks.dat", "rb")
records = pickle.load(file)
file.close()

for record in records:
    if record["roll"] == roll_no:
        record["marks"] = new_marks
        break

file = open("Data/marks.dat", "wb")
pickle.dump(records, file)
file.close()
print("Marks updated!")
