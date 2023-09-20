SELECT * FROM film ORDER BY film_id


UPDATE film
SET language_id = 5
WHERE film_id BETWEEN 10 AND 15

SELECT * FROM customer

-- IN customer table the foreign key define are store_id and address_id, if we want to insert in this table we have to know those values

DROP TABLE IF EXISTS customer_review;


SELECT * FROM rental 

SELECT * FROM rental
WHERE return_date IS NULL;

SELECT COUNT(*)
FROM rental
WHERE return_date IS NULL;





