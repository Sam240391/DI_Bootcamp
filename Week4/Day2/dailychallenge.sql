-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab



-- SELECT id FROM SecondTab WHERE id IS NULL
-- SELECT * FROM FirstTab WHERE id IS NULL

--  SELECT COUNT(*) 
--  FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

--  The query will return a count of 0 because the NULL id in FirstTab matches the NULL id in SecondTab.

-- SELECT COUNT(*) FROM FirstTab

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- THE OUTPUT is 2 because we want to count the row in firsttab excluding the rows with id equal to 5. and when we compare in with counter it's not take care about the NULL

-- SELECT id FROM SecondTab

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

--the Output is 0 because we compare we NULL ID 

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

--the Output is 2 because we compare with Id that no NULL in our case we have in the second tab the ID 5 
-- and we count the 6 and 7 on the first tab



