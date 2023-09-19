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



UPDATE students
SET birth_date = '1998-02-11'
WHERE first_name IN ('Lea', 'Marc') AND last_name = 'Benichou';


UPDATE students
SET last_name = 'Guez'
WHERE first_name IN ('David') AND last_name = 'Grez';

SELECT * FROM students

DELETE FROM students
WHERE first_name ='Lea' AND last_name ='Benichou'

SELECT COUNT(*) FROM students

SELECT COUNT(*) FROM students
WHERE birth_date >= '2000-01-01'


ALTER TABLE students ADD COLUMN math_grade INT;

SELECT * FROM students

UPDATE students 
SET math_grade = 80
WHERE id = 1
RETURNING 
    id,
    first_name, 
    last_name,
	birth_date,
	math_grade;
	
UPDATE students 
SET math_grade = 90
WHERE id IN (2,4)
RETURNING 
    id,
    first_name, 
    last_name,
	birth_date,
	math_grade;
	
UPDATE students 
SET math_grade = 40
WHERE id = 6
RETURNING 
    id,
    first_name, 
    last_name,
	birth_date,
	math_grade;
	
SELECT COUNT(*)as goods_students FROM students 
WHERE math_grade > 83
	
INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '1980-10-03', 70);


SELECT first_name, last_name, COUNT(math_grade) AS total_grades
FROM students
GROUP BY first_name, last_name;


SELECT SUM(math_grade) AS total_grades_sum
FROM students;

