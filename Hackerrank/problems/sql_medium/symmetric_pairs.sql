SELECT DISTINCT F.X, F.Y
FROM Functions F
WHERE 
(F.X < F.Y AND EXISTS (SELECT X, Y FROM Functions WHERE X=F.Y AND Y=F.X))
OR
(F.X = F.Y AND (SELECT COUNT(*) FROM Functions WHERE X=F.Y AND Y=F.X)>1)
ORDER BY F.X;