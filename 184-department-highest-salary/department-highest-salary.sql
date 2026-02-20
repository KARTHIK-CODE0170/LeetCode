/* Write your PL/SQL query statement below */
SELECT d.name AS department,e.name AS employee ,e.salary AS salary
FROM 
employee e
JOIN 
department d
ON e.departmentId = d.id
WHERE e.salary = (SELECT MAX(SALARY) FROM employee WHERE departmentId = e.departmentId);