# Python-MySQL Program 2: Fetch and display all records from Student table

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Student")

result = mycursor.fetchall()

print("Student Records:")
print("-" * 50)
for row in result:
    print("Admno:", row[0])
    print("Name:", row[1])
    print("Class:", row[2])
    print("Marks:", row[3])
    print("-" * 50)

mydb.close()
