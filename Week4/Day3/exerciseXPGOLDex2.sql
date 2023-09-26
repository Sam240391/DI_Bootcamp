SELECT * FROM store
SELECT COUNT(*) FROM store
SELECT * FROM inventory


SELECT s.store_id, ci.city, co.country 
FROM store as s
JOIN address as a
ON s.address_id = a.address_id
JOIN city as ci
ON a.city_id = ci.city_id
JOIN country as co
ON co.country_id = ci.country_id


SELECT * FROM film


SELECT i.store_id, SUM(f.length) as HOURS_OF_VIEWING
FROM film as f
JOIN inventory as i
ON f.film_id = i.film_id
GROUP BY i.store_id

SELECT * FROM rental WHERE return_date IS NULL
SELECT * FROM inventory

select p.store_id, SUM(p.length) from (SELECT DISTINCT i.store_id, f.film_id, f.length
FROM film as f
JOIN inventory as i
ON f.film_id = i.film_id
JOIN rental as r
ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL) as p
GROUP BY p.store_id


SELECT * FROM store
SELECT * FROM address


SELECT  c.first_name, c.last_name, c.store_id, a.address, a.address_id, ci.city, a.city_id
FROM customer as c
JOIN store as s
ON c.store_id = s.store_id
JOIN address as a
ON a.address_id = s.address_id
JOIN city as ci
ON ci.city_id = a.city_id
ORDER BY c.address_id






