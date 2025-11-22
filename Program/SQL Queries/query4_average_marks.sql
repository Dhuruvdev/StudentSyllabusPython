-- Query 4: Display the average marks of students in each class using GROUP BY

SELECT Class, AVG(Marks) AS Average_Marks FROM Student GROUP BY Class;
