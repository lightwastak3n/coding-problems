SET @max_problems=(SELECT COUNT(hacker_id) AS tot FROM Challenges GROUP BY hacker_id ORDER BY tot DESC LIMIT 1);
SELECT C.hacker_id AS id, H.name AS name, COUNT(*) AS challenges_created
FROM Challenges C
INNER JOIN Hackers H ON C.hacker_id= H.hacker_id
GROUP BY id, name
HAVING challenges_created = @max_problems OR
challenges_created IN (SELECT t.tot FROM (SELECT COUNT(*) AS tot FROM Challenges GROUP BY hacker_id) AS t GROUP BY t.tot HAVING COUNT(t.tot)=1)
ORDER BY challenges_created DESC, id;