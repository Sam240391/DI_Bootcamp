
SELECT * FROM customers
SELECT * FROM items

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    item_id INT REFERENCES items(item_id),
    quantity_purchased INT
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES
    ((SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'), 
     (SELECT item_id FROM items WHERE item_name = 'Fan'),
     1),
  
    ((SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'), 
     (SELECT item_id FROM items WHERE item_name = 'Large Desk'),
     10),
     
    ((SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'), 
     (SELECT item_id FROM items WHERE item_name = 'Small Desk'),
     2);
	 
SELECT * FROM purchases
SELECT * FROM customers
SELECT * FROM items

SELECT c.customer_id, c.first_name, c.last_name, p.quantity_purchased, p.item_id
FROM purchases as p
INNER JOIN customers as c
ON p.customer_id = c.customer_id;


SELECT c.customer_id, c.first_name, c.last_name, p.quantity_purchased, p.item_id, items.item_name, items.item_price
FROM purchases as p
INNER JOIN customers as c
ON p.customer_id = c.customer_id
INNER JOIN items
ON p.item_id = items.item_id
WHERE p.customer_id = 5;


SELECT c.customer_id, c.first_name, c.last_name, p.quantity_purchased, p.item_id, items.item_name, items.item_price
FROM purchases as p
INNER JOIN customers as c
ON p.customer_id = c.customer_id
INNER JOIN items
ON p.item_id = items.item_id
WHERE items.item_name IN ('Large Desk', 'Small Desk');


SELECT c.first_name, c.last_name, items.item_name
FROM purchases as p
INNER JOIN customers as c
ON p.customer_id = c.customer_id
INNER JOIN items
ON p.item_id = items.item_id



	 