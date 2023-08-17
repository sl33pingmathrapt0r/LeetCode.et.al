SELECT person_name
FROM Queue
WHERE turn=
(
  SELECT MAX(max.turn)
  FROM
  (
    SELECT q1.turn
    FROM Queue q1
    INNER JOIN Queue q2 ON q1.turn>=q2.turn -- -q1 person comes in after all q2 to this q1
    GROUP BY q1.turn
    HAVING SUM(q2.weight)<=1000
  ) as max
);

-- -OR replace Max on single column by limiting the original column return to only 1 row
SELECT person_name
FROM Queue
WHERE turn=
(
  SELECT q1.turn
  FROM Queue q1
  INNER JOIN Queue q2 ON q1.turn>=q2.turn -- -q1 person comes in after all q2 to this q1
  GROUP BY q1.turn
  HAVING SUM(q2.weight)<=1000
  ORDER BY SUM(q2.WEIGHT) DESC
  LIMIT 1
);
