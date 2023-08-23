SELECT T.user_id, ROUND(COALESCE(C.confirm/T.total, 0),2) as confirmation_rate
FROM
(
  SELECT s.user_id, COUNT(s.user_id) as total
  FROM Signups as s
  LEFT JOIN Confirmations as c ON s.user_id=c.user_id
  GROUP BY s.user_id
) as T
LEFT JOIN 
(
  SELECT s.user_id, COUNT(s.user_id) as confirm
  FROM Signups as s
  LEFT JOIN Confirmations as c ON s.user_id=c.user_id
  WHERE action="confirmed"
  GROUP BY s.user_id, action
) as C ON T.user_id=C.user_id;
