# Python-MySQL Program 1: Insert new student details into the database

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

admno = int(input("Enter Admission Number: "))
name = input("Enter Name: ")
class_name = input("Enter Class: ")
marks = int(input("Enter Marks: "))

sql = "INSERT INTO Student (Admno, Name, Class, Marks) VALUES (%s, %s, %s, %s)"
values = (admno, name, class_name, marks)

mycursor.execute(sql, values)
mydb.commit()

print("Record inserted successfully!")
print(mycursor.rowcount, "record inserted")

mydb.close()
