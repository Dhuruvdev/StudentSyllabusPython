# Program 6: Create CSV with user passwords and search

import csv

file = open("Data/users.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(["UserID", "Password"])
writer.writerow(["user1", "pass123"])
writer.writerow(["user2", "secret456"])
file.close()

userid = input("Enter User ID: ")
file = open("Data/users.csv", "r")
reader = csv.reader(file)
next(reader)

for row in reader:
    if row[0] == userid:
        print("Password:", row[1])
        break

file.close()
