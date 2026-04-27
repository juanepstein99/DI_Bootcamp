-- PART I
-- One to One relationship
-- =====================

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INTEGER UNIQUE REFERENCES customer(id)
);

-- Insert customers
INSERT INTO customer (first_name, last_name)
VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Insert profiles using subqueries
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES
(true, (SELECT id FROM customer WHERE first_name = 'John')),
(false, (SELECT id FROM customer WHERE first_name = 'Jerome'));

-- Logged in customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

-- All customers, even if they do not have a profile
SELECT c.first_name, cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp
ON c.id = cp.customer_id;

-- Number of customers that are not logged in
SELECT COUNT(*) AS not_logged_in_customers
FROM customer c
LEFT JOIN customer_profile cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = false OR cp.isLoggedIn IS NULL;