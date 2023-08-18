SELECT c1.visited_on, SUM(c2.amount) AS amount, ROUND(SUM(c2.amount)/7,2) AS average_amount
FROM (SELECT DISTINCT visited_on FROM Customer) c1
INNER JOIN Customer c2 ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on,INTERVAL 6 DAY) AND c1.visited_on
WHERE c1.visited_on>=(SELECT MIN(visited_on) FROM Customer)+6
GROUP BY c1.visited_on
ORDER BY c1.visited_on;
