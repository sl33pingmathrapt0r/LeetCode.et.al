SELECT id, SUM(num0) as num FROM
(
  (
    SELECT accepter_id as id, COUNT(requester_id) as num0
    FROM RequestAccepted
    GROUP BY accepter_id
    ORDER BY num0 DESC
  )
  UNION ALL
  (
    SELECT requester_id as id, COUNT(requester_id) as num0
    FROM RequestAccepted
    GROUP BY requester_id
    ORDER BY num0 DESC
  )
) as total
GROUP BY id
ORDER BY num DESC
LIMIT 1;

-- -OR
SELECT id, COUNT(*) as num
FROM
(
  (SELECT requester_id as id FROM RequestAccepted)
  UNION ALL
  (SELECT accepter_id as id FROM RequestAccepted)
) base
GROUP BY id
ORDER BY num DESC LIMIT 1;
