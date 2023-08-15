SELECT w1.id
FROM Weather as w1, Weather as w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate)=1 AND w1.temperature>w2.temperature;
