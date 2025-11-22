# Program 17: Program to maintain student record (Roll no, Name, Marks) using CSV file

import csv

def add_record():
    file = open("Sample_Data/students.csv", "a", newline='')
    writer = csv.writer(file)
    
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    writer.writerow([roll, name, marks])
    file.close()
    print("Record added successfully!")

def display_records():
    file = open("Sample_Data/students.csv", "r")
    reader = csv.reader(file)
    
    print("\nStudent Records:")
    for row in reader:
        print("Roll:", row[0], "Name:", row[1], "Marks:", row[2])
    
    file.close()

while True:
    print("\n1. Add Record")
    print("2. Display Records")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_record()
    elif choice == 2:
        display_records()
    elif choice == 3:
        break
    else:
        print("Invalid choice!")
