/* Write your PL/SQL query statement below */
SELECT name AS customers FROM Customers 
WHERE id NOT IN (SELECT customerId FROM Orders);