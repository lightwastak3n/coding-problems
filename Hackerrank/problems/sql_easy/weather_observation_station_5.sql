SELECT city, LENGTH(city) FROM station 
WHERE LENGTH(city) = (SELECT MAX(LENGTH(city)) FROM station) ORDER BY city ASC LIMIT 1;
SELECT city, LENGTH(city) FROM station 
WHERE LENGTH(city) = (SELECT MIN(LENGTH(city)) FROM station) ORDER BY city ASC LIMIT 1;