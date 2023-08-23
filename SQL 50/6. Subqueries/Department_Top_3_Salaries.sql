SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Department d
INNER JOIN Employee e ON d.id=e.departmentId
WHERE 
-- -find the employees who are in the top 3 salaries => there are less than 3 distinct salaries higher than them
(
    SELECT COUNT(DISTINCT salary)
    FROM Employee
    WHERE e.salary<salary AND e.departmentId=departmentId
) <3; 
