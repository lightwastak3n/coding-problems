SELECT t.hacker_id AS id, H.name AS name, SUM(max_score) AS total FROM
(SELECT hacker_id, challenge_id, MAX(score) AS max_score FROM Submissions GROUP BY hacker_id, challenge_id) AS t
INNER JOIN Hackers H ON t.hacker_id=H.hacker_id
GROUP BY id, name
HAVING total != 0
ORDER BY total DESC, id;