/* Write your PL/SQL query statement below */
SELECT max(salary) AS SecondHighestSalary  FROM Employee 
WHERE salary < (SELECT MAX(SALARY) FROM Employee) ;