SELECT *
FROM Cinema
WHERE id%2=1 AND id not in 
--Include NULL values-- -
    (
        SELECT id 
        FROM Cinema
        WHERE description="boring"
    )
ORDER BY rating DESC;
