SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT MIN(Doctor), MIN(Professor), MIN(Actor), MIN(Singer) 
FROM
(SELECT 
CASE
    WHEN occupation='Doctor' THEN @r1:=@r1+1
    WHEN occupation='Professor' THEN @r2:=@r2+1
    WHEN occupation='Actor' THEN @r3:=@r3+1
    WHEN occupation='Singer' THEN @r4:=@r4+1 END AS RowNumber,
CASE WHEN occupation='Doctor' THEN name END AS Doctor,
CASE WHEN occupation='Professor' THEN name END AS Professor,
CASE WHEN occupation='Actor' THEN name END AS Actor,
CASE WHEN occupation='Singer' THEN name END AS Singer
FROM occupations
ORDER BY name) AS t 
GROUP BY RowNumber;