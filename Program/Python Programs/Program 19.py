# Program 19: Display top 3 students

import csv

file = open("Data/students.csv", "r")
students = []
for row in csv.reader(file):
    try:
        students.append([row[0], row[1], int(row[2])])
    except:
        pass
file.close()

students.sort(key=lambda x: x[2], reverse=True)
print("Top 3 Students:")
for i in range(min(3, len(students))):
    print(students[i])
