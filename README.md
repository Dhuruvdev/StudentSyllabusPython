# Class XII Computer Science (083) Practical File (Session 2025-26)

This repository contains all practical programs for Class XII Computer Science as per the CBSE syllabus.

## Folder Structure

```
Program/
├── Python Programs/     (20 Programs - Part A)
├── SQL Queries/         (10 Queries - Part B)
└── Python-MySQL/        (5 Programs - Part C)

Data/                    (Test files)
Screenshots/             (Program screenshots with code and output)
```

## Part A: Python Programs (20 Programs)

### File Handling (Programs 1-8)

1. **program1_read_text_file.py** - Read a text file line by line and display each word separated by #
2. **program2_count_letters.py** - Count vowels, consonants, uppercase and lowercase letters in a text file
3. **program3_remove_lines.py** - Remove all lines containing the character ',' and write remaining lines to another file
4. **program4_binary_search_roll.py** - Create a binary file with names and roll numbers, then search for a roll number
5. **program5_binary_update_marks.py** - Create a binary file with roll number, name, and marks; update marks for a given roll number
6. **program6_csv_password_search.py** - Create a CSV file with user-id and password; search the password for a given user-id
7. **program7_csv_write_display.py** - Write data into a CSV file and display its contents
8. **program8_copy_file.py** - Program to copy content from one file to another

### Functions and Exception Handling (Programs 9-12)

9. **program9_factorial_recursion.py** - Program to calculate factorial using recursion
10. **program10_division_exception.py** - Program to handle division by zero using try-except
11. **program11_prime_check.py** - Program to check if a number is prime using a user-defined function
12. **program12_fibonacci_recursion.py** - Program to display Fibonacci sequence using recursion

### Data Structures - Stack (Programs 13-14)

13. **program13_stack_implementation.py** - Implement a stack using list with push() and pop() operations
14. **program14_palindrome_stack.py** - Program to check if a string is palindrome using stack logic

### Random & Miscellaneous (Programs 15-16)

15. **program15_dice_roll.py** - Simulate a dice roll using random module
16. **program16_password_generator.py** - Generate random passwords of given length

### CSV/Binary Applications (Programs 17-18)

17. **program17_student_record_csv.py** - Program to maintain student record (Roll no, Name, Marks) using CSV file
18. **program18_count_binary_records.py** - Count number of records in binary file

### Combined / Integrated Tasks (Programs 19-20)

19. **program19_top3_students.py** - Program to display the top 3 students from a marks file
20. **program20_merge_files.py** - Merge contents of two text files into one

## Part B: SQL Queries (10 Questions)

Assume a table Student (Admno INT PRIMARY KEY, Name VARCHAR(20), Class INT, Marks INT, Grade CHAR(2))

1. **query1_display_all.sql** - Display all records from the Student table
2. **query2_marks_greater_75.sql** - Display names and marks of students with marks greater than 75
3. **query3_order_by_name.sql** - Display all students in ascending order of Name
4. **query4_average_marks.sql** - Display the average marks of students in each class using GROUP BY
5. **query5_update_marks.sql** - Update marks of a student where Admno = 101
6. **query6_delete_low_marks.sql** - Delete records where marks < 40
7. **query7_add_column.sql** - Add a new column Address VARCHAR(30) in the Student table
8. **query8_count_grade_A.sql** - Display count of students having grade 'A'
9. **query9_max_min_marks.sql** - Display maximum and minimum marks from Student table
10. **query10_names_start_A.sql** - Display names of students whose name starts with 'A'

## Part C: Python-MySQL Connectivity (5 Programs)

Use `mysql.connector` module for all programs.

1. **mysql1_insert_record.py** - Insert new student details into the database
2. **mysql2_display_records.py** - Fetch and display all records from Student table
3. **mysql3_search_record.py** - Search a record by Admission number
4. **mysql4_update_marks.py** - Update marks for a specific student
5. **mysql5_delete_record.py** - Delete a record from Student table based on admission number

## How to Run Python Programs

1. Navigate to the respective folder:
   ```bash
   cd "Program/Python Programs"
   ```

2. Run any program using Python:
   ```bash
   python program1_read_text_file.py
   ```

## How to Run SQL Queries

1. Open your MySQL client or workbench
2. Load the SQL file or copy the query
3. Execute the query

## How to Run Python-MySQL Programs

1. Install mysql-connector-python:
   ```bash
   pip install mysql-connector-python
   ```

2. Make sure MySQL server is running
3. Update database connection details (host, user, password, database) in each program
4. Run the program:
   ```bash
   cd "Program/Python-MySQL"
   python mysql1_insert_record.py
   ```

## Screenshots

The `Screenshots/` folder contains PNG screenshots of all 20 Python programs showing code snippets and their output.

## Data Files

The `Data/` folder contains test files:
- sample.txt - For programs 1, 2
- input.txt - For program 3
- source.txt - For program 8
- file1.txt, file2.txt - For program 20
- Other files (CSV, binary) are created by the programs themselves

## Notes

- All programs are written in student-friendly style with simple variable names and comments
- Programs follow CBSE Class XII Computer Science syllabus
- Some programs create their own data files when run
- Make sure to have proper file permissions before running file handling programs

## Author

Class XII Student
Session 2025-26
