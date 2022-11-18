-- Using CASE
SELECT 
CASE 
	WHEN Grade > 7 THEN NAME
	ELSE "NULL"
END AS name, Grade, Marks
FROM Students, Grades
WHERE Marks BETWEEN Min_Mark and Max_Mark
ORDER BY GRADE DESC, Name, Marks;

-- Using IF
SELECT IF(Grade > 7, Name, "NULL"), Grade, Marks
FROM Students, Grades
WHERE Marks BETWEEN Min_Mark and Max_Mark
ORDER BY GRADE DESC, Name, Marks;