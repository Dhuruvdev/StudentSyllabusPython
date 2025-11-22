# Program 19: Program to display the top 3 students from a marks file

import csv

file = open("Data/students.csv", "r")
reader = csv.reader(file)

students = []
for row in reader:
    students.append([row[0], row[1], int(row[2])])

file.close()

students.sort(key=lambda x: x[2], reverse=True)

print("Top 3 Students:")
for i in range(min(3, len(students))):
    print("Roll:", students[i][0], "Name:", students[i][1], "Marks:", students[i][2])
