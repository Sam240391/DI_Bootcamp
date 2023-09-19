-- CREATE TABLE students (
--     id SERIAL PRIMARY KEY,
--     last_name VARCHAR(50),
--     first_name VARCHAR(50),
--     birth_date DATE
-- );

-- INSERT INTO students (first_name, last_name, birth_date) 
-- VALUES
--     ('Marc', 'Benichou', '02/11/1998'),
--     ('Yoan', 'Cohen', '03/12/2010'),
--     ('Lea', 'Benichou', '27/07/1987'),
--     ('Amelia', 'Dux', '	07/04/1996'),
--     ('David', 'Grez', '14/06/2003'),
--     ('Omer', 'Simpson', '03/10/1980');




-- SELECT first_name, last_name, birth_date
-- FROM students
-- ORDER BY last_name
-- FETCH NEXT 4 ROWS ONLY

-- SELECT first_name, last_name, birth_date
-- FROM students
-- ORDER BY birth_date DESC
-- LIMIT 1;

-- SELECT first_name, last_name, birth_date
-- FROM students
-- LIMIT 3 OFFSET 2;





