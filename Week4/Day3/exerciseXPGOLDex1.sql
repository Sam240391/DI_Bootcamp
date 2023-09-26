-- SELECT * FROM film

-- SELECT * FROM rental WHERE return_date IS NULL;

-- SELECT  f.title, c.first_name, c.last_name, r.rental_date, r.return_date 
-- FROM film as f
-- JOIN inventory as i
-- ON f.film_id = i.film_id
-- JOIN rental as r
-- ON i.inventory_id = r.inventory_id
-- JOIN customer as c
-- ON r.customer_id = c.customer_id
-- WHERE r.return_date IS NULL

-- SELECT f.title, fr
-- FROM film as f
-- JOIN film_category as fr
-- ON f.film_id = fr.film_id
-- JOIN category as c
-- on c.category_id = fr.category_id

-- WHERE c.name = 'Action';

-- SELECT *
-- FROM category as ca
-- JOIN film_category as fc
-- ON ca.category_id = fc.category_id
-- JOIN film as f
-- ON fc.film_id = f.film_id
-- JOIN film_actor as fa
-- ON f.film_id = fa.film_id
-- JOIN actor as a
-- ON a.actor_id = fa.actor_id
-- WHERE ca.name = 'Action' AND a.first_name = 'Joe' AND a.last_name = 'Swank'
