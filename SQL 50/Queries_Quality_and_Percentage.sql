SELECT Queries.query_name, ROUND(AVG(rating/position),2) AS quality, IFNULL(ROUND((poor/COUNT(rating))*100.0, 2),0) AS poor_query_percentage
FROM Queries
LEFT JOIN
(
    SELECT query_name, COUNT(query_name) as poor
    FROM Queries
    WHERE rating<3
    GROUP BY query_name
) as Poor ON Queries.query_name=Poor.query_name
GROUP BY Queries.query_name;

--OR-- -
select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;
