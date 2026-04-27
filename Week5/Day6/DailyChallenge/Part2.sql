-- PART II
-- Many to Many relationship
-- =====================

CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- Insert books
INSERT INTO book (title, author)
VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INTEGER CHECK (age <= 15)
);

-- Insert students
INSERT INTO student (name, age)
VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

CREATE TABLE library (
    book_fk_id INTEGER REFERENCES book(book_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

    student_fk_id INTEGER REFERENCES student(student_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

    borrowed_date DATE,

    PRIMARY KEY (book_fk_id, student_fk_id)
);

-- Insert records using subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES
(
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'John'),
    '2022-02-15'
),
(
    (SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-03-03'
),
(
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'Lera'),
    '2021-05-23'
),
(
    (SELECT book_id FROM book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-08-12'
);

-- Select all columns from the junction table
SELECT *
FROM library;

-- Select student names and borrowed book titles
SELECT s.name, b.title
FROM library l
JOIN student s
ON l.student_fk_id = s.student_id
JOIN book b
ON l.book_fk_id = b.book_id;

-- Average age of children who borrowed Alice In Wonderland
SELECT AVG(s.age) AS average_age
FROM library l
JOIN student s
ON l.student_fk_id = s.student_id
JOIN book b
ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- Delete a student
DELETE FROM student
WHERE name = 'John';

-- Check what happened in the junction table
-- John's records are deleted automatically because of ON DELETE CASCADE
SELECT *
FROM library;