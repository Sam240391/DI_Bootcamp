-- SELECT * FROM film ORDER BY film_id


-- UPDATE film
-- SET language_id = 5
-- WHERE film_id BETWEEN 10 AND 15

-- SELECT * FROM customer

-- -- IN customer table the foreign key define are store_id and address_id, if we want to insert in this table we have to know those values

-- DROP TABLE IF EXISTS customer_review;

-- SELECT * FROM rental 

-- SELECT * FROM rental
-- WHERE return_date IS NULL;

-- SELECT COUNT(*)
-- FROM rental
-- WHERE return_date IS NULL;

-- SELECT * FROM rental
-- SELECT * FROM film
-- SELECT * FROM inventory

-- WE HAVE TO JOIN THOSE 3 TABLES IN ORDER TO GET OUR DATA

-- SELECT f.title, r.return_date, f.replacement_cost
-- FROM rental as r
-- JOIN inventory as i
-- ON  r.inventory_id = i.inventory_id
-- JOIN film as f
-- ON f.film_id = i.film_id
-- WHERE return_date IS NULL
-- ORDER BY replacement_cost DESC
-- LIMIT 30;


-- SELECT * FROM film
-- SELECT * from film_actor where actor_id = 120
-- SELECT * from actor where first_name = 'Penelope'


-- SELECT title, description
-- FROM film
-- WHERE description LIKE '%sumo%' AND film_id IN (SELECT film_id FROM film_actor WHERE actor_id IN (SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe')
-- );

-- SELECT title, length, rating
-- FROM film
-- WHERE length < 60 AND rating = 'R';


-- SELECT DISTINCT f.film_id, f.title, c.first_name, c.last_name, r.rental_date, r.return_date, p.amount
-- FROM film as f
-- JOIN inventory as i
-- ON f.film_id = i.film_id
-- JOIN rental as r
-- ON i.inventory_id = r.inventory_id
-- JOIN customer as c
-- ON c.customer_id = r.customer_id
-- JOIN payment as p
-- ON p.customer_id = c.customer_id
-- WHERE first_name = 'Matthew' and last_name = 'Mahan' AND amount > 4 AND return_date BETWEEN '2005-07-28' and '2005-08-01';



-- SELECT f.film_id, f.title, f.description, f.replacement_cost, c.first_name, c.last_name, r.rental_date, r.return_date, p.amount
-- FROM film as f
-- JOIN inventory as i
-- ON f.film_id = i.film_id
-- JOIN rental as r
-- ON i.inventory_id = r.inventory_id
-- JOIN customer as c
-- ON c.customer_id = r.customer_id
-- JOIN payment as p
-- ON p.customer_id = c.customer_id
-- WHERE first_name = 'Matthew' AND last_name = 'Mahan' 
-- AND amount > 4 AND return_date BETWEEN '2005-07-28' and '2005-08-01' AND (title LIKE '%boat%' OR description LIKE '%boat%') AND replacement_cost > 30;

