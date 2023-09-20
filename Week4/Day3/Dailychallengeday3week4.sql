-- CREATE TABLE customer(
-- 	id SERIAL PRIMARY KEY, 
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE customer_Profile (
--     id SERIAL PRIMARY KEY,
--     isLoggedIn BOOLEAN DEFAULT false,
--     customer_id INT REFERENCES customer(id)
-- );


-- INSERT INTO customer (first_name, last_name) 
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- INSERT INTO customer_Profile (isLoggedIn, customer_id) 
-- VALUES
-- (true, (SELECT id FROM customer WHERE first_name = 'John')),
-- (false, (SELECT id FROM customer WHERE first_name = 'Jerome'));


-- SELECT c.first_name
-- FROM customer as c
-- JOIN customer_Profile as cp 
-- ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = true;


-- SELECT c.first_name, cp.isLoggedIn
-- FROM customer as c
-- LEFT JOIN customer_Profile as cp 
-- ON c.id = cp.customer_id;


-- SELECT COUNT(*) 
-- FROM customer as c
-- JOIN customer_Profile as cp 
-- ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = false;


-- CREATE TABLE Book(
-- 	book_id SERIAL PRIMARY KEY,
-- 	title VARCHAR(50) NOT NULL,
-- 	author VARCHAR(50) NOT NULL
-- );

-- INSERT INTO Book (title, author)
-- VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K. Rowling'),
-- ('To Kill a Mockingbird', 'Harper Lee');

-- CREATE TABLE Student(
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL UNIQUE,
-- 	age INT check (age <= 15)
-- );

-- INSERT INTO Student (name, age) 
-- VALUES
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);


-- CREATE TABLE Library (
--     book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id)
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
-- ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
-- ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

-- SELECT * FROM Library


SELECT s.name, b.title
FROM Student s
JOIN Library l ON s.student_id = l.student_fk_id
JOIN Book b ON l.book_fk_id = b.book_id;


-- SELECT AVG(s.age)
-- FROM Student s
-- JOIN Library l 
-- ON s.student_id = l.student_fk_id
-- JOIN Book b 
-- ON l.book_fk_id = b.book_id
-- WHERE b.title = 'Alice In Wonderland';


-- DELETE FROM Student WHERE name = 'John';

-- SELECT s.name, b.title
-- FROM Student s
-- JOIN Library l ON s.student_id = l.student_fk_id
-- JOIN Book b ON l.book_fk_id = b.book_id;

-- SELECT * FROM Library

-- WE CAN CHECK THAT THE STUDENT JOHN HAS BEEN ALSO DELETED INTO THE OTHER TABLE WHERE THE STUDENT ID WAS AS FOREIGN KEY




