/* Write your PL/SQL query statement below */
SELECT name as customers 
FROM 
orders
RIGHT JOIN
customers
ON orders.customerId = customers.id
WHERE orders.id IS NULL;
