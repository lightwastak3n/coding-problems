SET @stars = 0;
SELECT REPEAT("* ", @stars := @stars + 1)
FROM INFORMATION_SCHEMA.TABLES LIMIT 20;