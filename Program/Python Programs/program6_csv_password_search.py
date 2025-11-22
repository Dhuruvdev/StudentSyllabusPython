# Program 6: Create a CSV file with user-id and password; search the password for a given user-id

import csv

def create_csv():
    file = open("Sample_Data/users.csv", "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["UserID", "Password"])
    writer.writerow(["user1", "pass123"])
    writer.writerow(["user2", "secret456"])
    writer.writerow(["user3", "mypass789"])
    file.close()
    print("CSV file created!")

def search_password():
    userid = input("Enter User ID: ")
    file = open("Sample_Data/users.csv", "r")
    reader = csv.reader(file)
    next(reader)
    
    found = False
    for row in reader:
        if row[0] == userid:
            print("Password for", userid, "is:", row[1])
            found = True
            break
    
    if not found:
        print("User ID not found!")
    
    file.close()

create_csv()
search_password()
