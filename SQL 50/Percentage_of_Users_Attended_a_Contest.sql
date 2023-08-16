SELECT contest_id, ROUND(COUNT(contest_id)/total*100.0,2) AS percentage
FROM 
(
    SELECT COUNT(user_id) as total
    FROM Users
) AS Total, Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;
