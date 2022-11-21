SELECT Start_Date, MIN(End_Date)
FROM 
(SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) AS S,
(SELECT End_Date FROM PROJECTS WHERE End_Date NOT IN (SELECT Start_Date FROM PROJECTS)) AS E
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY DATEDIFF(Start_Date, MIN(End_Date)) DESC, Start_Date;