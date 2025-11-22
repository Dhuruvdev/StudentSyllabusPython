# Python-MySQL Program 4: Update marks for a specific student

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

admno = int(input("Enter Admission Number: "))
new_marks = int(input("Enter new marks: "))

sql = "UPDATE Student SET Marks = %s WHERE Admno = %s"
values = (new_marks, admno)

mycursor.execute(sql, values)
mydb.commit()

print(mycursor.rowcount, "record(s) updated")

mydb.close()
