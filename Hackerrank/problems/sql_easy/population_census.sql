SELECT SUM(city.population) 
FROM city 
INNER JOIN country ON city.countryCode = country.code 
WHERE country.continent = "Asia";