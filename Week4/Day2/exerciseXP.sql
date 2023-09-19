-- SELECT * FROM customer

-- SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- SELECT DISTINCT create_date FROM customer 

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT * FROM film

-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

-- SELECT * FROM customer
-- SELECT * FROM address

-- SELECT address, phone FROM address WHERE district = 'Texas'

-- SELECT * FROM film

-- SELECT * FROM film WHERE film_id IN (15, 150);

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Desire Alien';

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Bi%';

-- SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;

-- SELECT * FROM film ORDER BY rental_rate ASC FETCH NEXT 10 ROWS ONLY; 


-- SELECT * FROM customer
-- SELECT * FROM payment

-- SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
-- FROM customer as c
-- JOIN payment as p 
-- ON c.customer_id = p.customer_id
-- ORDER BY p.customer_id;

-- SELECT * FROM inventory

-- SELECT DISTINCT film_id FROM inventory

-- SELECT film_id, title FROM film
-- WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);

-- SELECT city.city, country.country 
-- FROM city
-- JOIN country 
-- ON city.country_id = country.country_id;


-- SELECT p.staff_id, c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
-- FROM customer c
-- JOIN payment p ON c.customer_id = p.customer_id
-- ORDER BY p.staff_id;


