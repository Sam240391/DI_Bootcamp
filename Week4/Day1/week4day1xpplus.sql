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

-- select * from students

-- select first_name, last_name from students

-- SELECT * FROM students WHERE id = 2;

-- SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';


-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '_a%a';

-- SELECT first_name, last_name FROM students WHERE id IN (1, 3);

-- SELECT * FROM students WHERE birth_date >= '2000-01-01';









