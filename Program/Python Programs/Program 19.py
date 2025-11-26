# Program 19: Display student records

import csv

file = open("Data/students.csv", "r")
reader = csv.reader(file)

print("Student Records:")
count = 0
for row in reader:
    print(row)
    count += 1
    if count == 3:
        break

file.close()
