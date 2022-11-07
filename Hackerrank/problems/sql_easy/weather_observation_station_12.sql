SELECT DISTINCT city FROM station WHERE city REGEXP "^[^aeiou].*[^aeiou]$";
-- Without regex
SELECT DISTINCT city FROM station WHERE RIGHT(city,1) NOT IN ("a", "e", "i", "o", "u") AND LEFT(city,1) NOT IN ("a", "e", "i", "o", "u");