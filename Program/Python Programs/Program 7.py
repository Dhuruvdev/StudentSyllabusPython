# Program 7: Write data to CSV and display

import csv

file = open("Data/data.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(["Name", "Age", "City"])
writer.writerow(["Rohan", 18, "Delhi"])
writer.writerow(["Meera", 17, "Mumbai"])
file.close()

file = open("Data/data.csv", "r")
reader = csv.reader(file)
print("CSV Contents:")
for row in reader:
    print(row)
file.close()
