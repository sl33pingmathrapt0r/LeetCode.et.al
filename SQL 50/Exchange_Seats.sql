SELECT IF(
    id%2, 
    IF(
        id<>(SELECT MAX(id) FROM Seat), 
        id+1, 
        id
    ), 
    id-1
) AS id, student
FROM Seat
ORDER BY id;

-- -OR use CASE
SELECT 
(
    CASE WHEN id%2 THEN
    (
        CASE WHEN id<>(SELECT MAX(id) FROM Seat) THEN
        id+1
        ELSE id END
    )
    ELSE id-1 END
) AS id, student
FROM Seat
ORDER BY id;
