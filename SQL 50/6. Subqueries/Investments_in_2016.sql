SELECT ROUND(SUM(tiv_2016),2) as tiv_2016
FROM Insurance
WHERE pid IN
(
  (
    SELECT DISTINCT i1.pid
    FROM Insurance i1
    INNER JOIN Insurance i2 ON i1.tiv_2015=i2.tiv_2015 and i1.pid<>i2.pid
  )
  EXCEPT
  (
    SELECT DISTINCT i1.pid 
    FROM Insurance i1
    INNER JOIN Insurance i2 ON i1.lat=i2.lat AND i1.lon=i2.lon AND i1.pid<>i2.pid
  )
);
