SET @stars = 21;
SELECT REPEAT("* ", @stars := @stars - 1)
FROM INFORMATION_SCHEMA.TABLES;