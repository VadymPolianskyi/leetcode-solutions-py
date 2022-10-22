-- Table: Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table contains an email. The emails will not contain uppercase letters.

-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.

-- Solution 1 (slow)
SELECT DISTINCT p1.email Email
FROM Person p1
    INNER JOIN Person p2
    ON p1.id != p2.id AND p1.email = p2.email;

-- Solution 2 (fast)
SELECT email Email
FROM Person
GROUP BY email
HAVING count(*) > 1
