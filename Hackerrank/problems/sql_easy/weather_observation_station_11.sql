SELECT DISTINCT city FROM station WHERE city REGEXP "^[^aeiou]|[^aeiou]$";
-- Without regex
SELECT DISTINCT city FROM station WHERE RIGHT(city,1) NOT IN ("a", "e", "i", "o", "u") OR LEFT(city,1) NOT IN ("a", "e", "i", "o", "u");