SELECT ROUND(COUNT(DISTINCT Activity.player_id)/total,2) AS fraction
FROM Activity
LEFT JOIN (
    SELECT player_id, MIN(event_date) as day1
    FROM Activity
    GROUP BY player_id
) AS D on Activity.player_id=D.player_id
CROSS JOIN (
    SELECT COUNT(DISTINCT player_id) AS total
    FROM Activity
) AS T
WHERE DATEDIFF(event_date, day1)=1;


--OR BETTER-- -

SELECT IFNULL(
    ROUND(
        COUNT(
            DISTINCT Activity.player_id)/
            (
                SELECT COUNT(DISTINCT player_id)
                FROM Activity
            )
        ,2)
    ,0) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN
    (
        SELECT player_id, MIN(event_date) as day1
        FROM Activity
        GROUP BY player_id
    );
