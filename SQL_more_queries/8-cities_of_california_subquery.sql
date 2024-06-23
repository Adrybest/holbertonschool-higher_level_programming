-- script that lists all the cities of California
-- 8-cities_of_california_subquery.sql
SELECT id, name
  FROM cities
 WHERE state_id IN
       (SELECT id
	  FROM states
	 WHERE name = "California")