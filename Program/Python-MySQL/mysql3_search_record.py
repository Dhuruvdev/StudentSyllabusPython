# Python-MySQL Program 3: Search a record by Admission number

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

admno = int(input("Enter Admission Number to search: "))

sql = "SELECT * FROM Student WHERE Admno = %s"
values = (admno,)

mycursor.execute(sql, values)

result = mycursor.fetchone()

if result:
    print("\nStudent Found:")
    print("Admno:", result[0])
    print("Name:", result[1])
    print("Class:", result[2])
    print("Marks:", result[3])
else:
    print("No student found with Admno:", admno)

mydb.close()
