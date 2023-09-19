SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating;

SELECT * FROM film WHERE rating IN ('G', 'PG-13') AND length < 120 AND rental_rate < 3.00
ORDER BY title;


UPDATE customer
SET first_name = 'Samuel',
    last_name = 'CHEMLA',
    email = 'samuelchemla24@gmail.com'
WHERE customer_id = 4;

SELECT * FROM customer ORDER BY customer_id
SELECT * FROM address ORDER BY address_id

SELECT address_id FROM customer WHERE customer_id = 4

Select address from address where address_id = (SELECT address_id FROM customer where customer_id = 4)


UPDATE address
SET address = '2 rue de la paix'
WHERE address_id = (SELECT address_id FROM customer where customer_id = 4);


