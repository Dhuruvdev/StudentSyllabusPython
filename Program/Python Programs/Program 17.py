# Program 17: Student records with CSV

import csv

def add_record():
    file = open("Data/students.csv", "a", newline='')
    writer = csv.writer(file)
    roll = int(input("Roll: "))
    name = input("Name: ")
    marks = int(input("Marks: "))
    writer.writerow([roll, name, marks])
    file.close()
    print("Record added")

def display():
    file = open("Data/students.csv", "r")
    for row in csv.reader(file):
        print(row)
    file.close()

while True:
    print("\n1. Add  2. Display  3. Exit")
    choice = int(input("Choice: "))
    if choice == 1:
        add_record()
    elif choice == 2:
        display()
    elif choice == 3:
        break
