# Program 17: Simple student record demo with CSV

import csv

file = open("Data/students.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow([1, "Rohan", 85])
writer.writerow([2, "Priya", 90])
file.close()

file = open("Data/students.csv", "r")
for row in csv.reader(file):
    print(row)
file.close()
