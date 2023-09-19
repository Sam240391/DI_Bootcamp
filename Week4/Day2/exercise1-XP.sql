-- CREATE TABLE items (
--     item_id SERIAL PRIMARY KEY,
--     item_name VARCHAR(255) NOT NULL,
--     item_price DECIMAL(10, 2) NOT NULL
-- );

-- INSERT INTO items (item_name, item_price) 
-- VALUES
--     ('Small Desk', 100),
--     ('Large Desk', 300),
--     ('Fan', 80);
	
-- CREATE TABLE customers (
--     customer_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(255) NOT NULL,
--     last_name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO customers (first_name, last_name) 
-- VALUES
--     ('Greg', 'Jones'),
--     ('Sandra', 'Jones'),
--     ('Scott', 'Scott'),
--     ('Trevor', 'Green'),
--     ('Melanie', 'Johnson');


-- SELECT * FROM items ORDER BY item_price;

-- SELECT * FROM items WHERE item_price >= 80 ORDER BY item_price DESC;

-- SELECT last_name, first_name FROM customers ORDER BY first_name ASC LIMIT 3

-- SELECT last_name FROM customers ORDER BY last_name DESC
