-- lists all databases of MySQL server
-- using commnad
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
