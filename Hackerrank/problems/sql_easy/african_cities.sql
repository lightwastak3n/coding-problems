SELECT city.name FROM city 
INNER JOIN country ON city.countryCode = country.code 
WHERE country.continent = "Africa";