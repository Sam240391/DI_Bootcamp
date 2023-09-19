-- SELECT * FROM language

-- SELECT * FROM film

-- SELECT f.title, f.description, l.name
-- FROM film as f
-- JOIN language as l 
-- ON f.language_id = l.language_id


-- SELECT f.title, f.description, l.name
-- FROM language as l
-- LEFT JOIN film as f
-- ON f.language_id = l.language_id

-- CREATE TABLE new_film(
	
-- 	new_film_id SERIAL PRIMARY KEY, 
-- 	new_film_name VARCHAR(50)
	
-- );


-- INSERT INTO new_film (new_film_name)
-- VALUES
--     ('Return to the Future'),
--     ('Harry Potter');


-- CREATE TABLE customer_review(
	
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INT REFERENCES new_film(new_film_id) ON DELETE CASCADE,
-- 	language_id INT REFERENCES language(language_id),
-- 	title VARCHAR(50),
--     score INT CHECK (score >= 1 AND score <= 10),
--     review_text TEXT,
--     last_update TIMESTAMP
	
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES
--     (1, 1, 'Review 1', 8, 'This is a good film.', NOW()),
--     (1, 1, 'Review 2', 7, 'Enjoyable movie.', NOW()),
-- 	(2, 1, 'Review 2', 1, 'Bad Movie', NOW()),
-- 	(2, 1, 'Review 2', 2, 'not recommended', NOW())
-- ;

-- SELECT * FROM customer_review


-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES
--     (1, 5, 'Review 5', 8, 'Tres bon film', NOW())
-- ;


-- DELETE FROM new_film
-- WHERE new_film_id = 1;




