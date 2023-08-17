-- -TRIANGLE INEQUALITY
SELECT *, CASE WHEN (x+y>z and x+z>y and y+z>x) THEN 'Yes' ELSE 'No' END as triangle
FROM Triangle;

-- -OR
SELECT *, IF(x+y>z and x+z>y and y+z>x, 'Yes', 'No') as triangle
FROM Triangle;
