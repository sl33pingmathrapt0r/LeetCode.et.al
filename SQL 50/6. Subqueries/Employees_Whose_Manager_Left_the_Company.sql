SELECT employee_id
FROM Employees
WHERE salary<30000 AND NOT ISNULL(manager_id) AND employee_id NOT IN
(
    SELECT e1.employee_id
    FROM Employees e1
    INNER JOIN Employees e2 ON e1.manager_id=e2.employee_id
)
ORDER BY employee_id;
