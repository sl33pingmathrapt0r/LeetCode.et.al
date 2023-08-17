SELECT L1.num AS ConsecutiveNums
FROM Logs L1, Logs L2, Logs L3
WHERE L1.id + 1=L2.id and L2.id+1=L3.id AND L1.num=L2.num and L2.num=L3.num
GROUP BY L1.num;
