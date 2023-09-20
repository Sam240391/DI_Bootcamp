-- CREATE TABLE users (
--     user_id SERIAL PRIMARY KEY,
--     username VARCHAR(255) UNIQUE
-- );

-- CREATE TABLE product_orders (
--     order_id SERIAL PRIMARY KEY,
--     order_date DATE,
--     user_id INT REFERENCES users(user_id)
-- );

-- CREATE TABLE items (
--     item_id SERIAL PRIMARY KEY,
--     order_id INT REFERENCES product_orders(order_id),
--     product_name VARCHAR(255),
--     quantity INT,
--     price DECIMAL(10, 2)
-- );


-- INSERT INTO users (username) VALUES ('John'), ('David');

-- INSERT INTO product_orders (order_date, user_id) VALUES
-- ('2023-09-15', 1),
-- ('2023-09-16', 1),
-- ('2023-09-16', 2);

-- INSERT INTO items (order_id, product_name, quantity, price) VALUES
-- (1, 'Product A', 2, 10.99),
-- (1, 'Product B', 1, 5.99),
-- (2, 'Product C', 3, 7.49),
-- (3, 'Product D', 1, 12.99);


SELECT * FROM items
SELECT order_id FROM product_orders where user_id = 1
SELECT * FROM users

select calculate_order_total(order_id) FROM product_orders where user_id = 1;
select sum(calculate_order_total(order_id)) FROM product_orders where user_id = 1;


CREATE OR REPLACE FUNCTION calculate_order_total(order_id INT)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total_price DECIMAL(10, 2) := 0;
BEGIN
    SELECT SUM(i.price * i.quantity) INTO total_price
    FROM items as i
    WHERE i.order_id = calculate_order_total.order_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;


SELECT calculate_order_total(1);












