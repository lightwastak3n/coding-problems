SELECT id, age, coins_needed, power
FROM Wands W
INNER JOIN Wands_Property WP ON W.code = WP.code
WHERE is_evil = 0 AND
coins_needed = (
    SELECT MIN(coins_needed) 
    FROM Wands Wa 
    INNER JOIN Wands_Property WPr ON Wa.code = WPr.code
    WHERE Wa.power = W.power AND WPr.age = WP.age)
ORDER BY power DESC, age DESC;