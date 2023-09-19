SELECT * FROM customers

SELECT first_name ||' '|| last_name as full_name FROM customers ORDER BY last_name DESC
LIMIT 2

DELETE FROM purchases
WHERE (customer_id = (SELECT customer_id FROM customers WHERE first_name = 'Scott'))

SELECT * FROM purchases

-- YES SCOTT still exist in the customers table

SELECT * FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott';


SELECT p.id AS "Purchase ID", 
       CASE WHEN c.first_name IS NULL THEN '' ELSE c.first_name END AS "Customer First Name", 
       CASE WHEN c.last_name IS NULL THEN '' ELSE c.last_name END AS "Customer Last Name", 
       items.item_name AS "Item Name"
FROM purchases p
LEFT JOIN customers c 
ON p.customer_id = c.customer_id
LEFT JOIN items 
ON p.item_id = items.item_id;




SELECT p.id AS "Purchase ID", 
       c.first_name AS "Customer First Name", 
       c.last_name AS "Customer Last Name", 
       items.item_name AS "Item Name"
FROM purchases as p
INNER JOIN customers as c 
ON p.customer_id = c.customer_id
INNER JOIN items 
ON p.item_id = items.item_id
