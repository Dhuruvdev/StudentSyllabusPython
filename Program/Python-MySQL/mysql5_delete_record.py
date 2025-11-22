# Python-MySQL Program 5: Delete a record from Student table based on admission number

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

admno = int(input("Enter Admission Number to delete: "))

sql = "DELETE FROM Student WHERE Admno = %s"
values = (admno,)

mycursor.execute(sql, values)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

mydb.close()
