CREATE TABLE items (
  id SERIAL PRIMARY key,
  name text,
  price integer
)

-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

INSERT INTO items (name, price)
values
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  first_name text,
  last_name text
);

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

INSERT INTO customers (first_name, last_name)
values
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

-- 1.All the items.
SELECT name FROM items;

-- 2.All the items with a price above 80 (80 not included).
SELECT * 
FROM items 
WHERE price > 80

-- 3.All the items with a price below 300. (300 included)
SELECT *
FROM items
WHERE price <= 300;

-- 4.All customers whose last name is 'Smith' (What will be your outcome?).
SELECT * 
FROM customers
WHERE last_name = 'Smith';
-- Outcome = Success. No rows returned

-- 5.All customers whose last name is 'Jones'.
SELECT * 
FROM customers
WHERE last_name = 'Jones';

-- 6. All customers whose firstname is not 'Scott'
SELECT * 
FROM customers
WHERE first_name != 'Scott';