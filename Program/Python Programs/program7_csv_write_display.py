# Program 7: Write data into a CSV file and display its contents

import csv

file = open("Sample_Data/data.csv", "w", newline='')
writer = csv.writer(file)

writer.writerow(["Name", "Age", "City"])
writer.writerow(["Rohan", 18, "Delhi"])
writer.writerow(["Meera", 17, "Mumbai"])
writer.writerow(["Vijay", 18, "Bangalore"])

file.close()
print("Data written to CSV file!\n")

print("Contents of CSV file:")
file = open("Sample_Data/data.csv", "r")
reader = csv.reader(file)

for row in reader:
    print(row)

file.close()
