CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08-10-1970', 5);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06-05-1961', 2);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Angelina','Jolie','1975-06-04', 1);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Jennifer','Aniston','1969-08-10', 0);

-- 1. Count how many actors are in the table.
SELECT COUNT (*)
FROM actors;

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
INSERT INTO actors (first_name, last_name)
VALUES ('Brad', 'Pitt');
-- “If I try to insert a new actor with blank fields, 
-- it will cause an error because those columns have a NOT NULL constraint, so the record won’t be inserted.”