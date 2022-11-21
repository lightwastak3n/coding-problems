SELECT S.Name
FROM Students AS S
WHERE (SELECT Salary FROM Packages WHERE ID=(SELECT ID FROM Students WHERE Name=S.Name)) <
(SELECT Salary FROM Packages WHERE ID=(SELECT Friend_ID FROM Friends WHERE ID=(SELECT ID FROM Students WHERE Name=S.Name)))
ORDER BY (SELECT Salary FROM Packages WHERE ID=(SELECT Friend_ID FROM Friends WHERE ID=(SELECT ID FROM Students WHERE Name=S.Name)));