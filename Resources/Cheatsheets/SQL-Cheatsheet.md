# SQL Cheatsheet

A quick reference for SQL queries, data manipulation, and database management.

## Table of Contents
- [Data Query Language (SELECT)](#data-query-language-select)
- [Filtering & Sorting](#filtering--sorting)
- [Joins](#joins)
- [Aggregation & Grouping](#aggregation--grouping)
- [Data Manipulation (INSERT, UPDATE, DELETE)](#data-manipulation-insert-update-delete)
- [Data Definition (CREATE, ALTER, DROP)](#data-definition-create-alter-drop)
- [Indexes & Constraints](#indexes--constraints)
- [Subqueries & CTEs](#subqueries--ctes)
- [Window Functions](#window-functions)

---

## Data Query Language (SELECT)

Retrieve data from one or more tables.

```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, name, email FROM users;

-- Select with alias
SELECT id, first_name AS name, email AS contact FROM users;

-- Select distinct values
SELECT DISTINCT country FROM users;

-- Limit results
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;  -- pagination

-- Select with calculated column
SELECT name, price, price * 0.9 AS discounted_price FROM products;
```

---

## Filtering & Sorting

Narrow down and order query results.

```sql
-- Basic WHERE clause
SELECT * FROM users WHERE active = true;

-- Comparison operators
SELECT * FROM products WHERE price > 50;
SELECT * FROM orders WHERE created_at >= '2024-01-01';

-- Multiple conditions
SELECT * FROM users WHERE age >= 18 AND country = 'US';
SELECT * FROM users WHERE role = 'admin' OR role = 'moderator';

-- NOT operator
SELECT * FROM users WHERE NOT active = false;

-- IN operator
SELECT * FROM users WHERE country IN ('US', 'CA', 'UK');

-- BETWEEN operator
SELECT * FROM products WHERE price BETWEEN 10 AND 100;

-- LIKE pattern matching
SELECT * FROM users WHERE email LIKE '%@gmail.com';
SELECT * FROM users WHERE name LIKE 'J%';    -- starts with J
SELECT * FROM users WHERE name LIKE '%son';  -- ends with son

-- NULL checks
SELECT * FROM users WHERE phone IS NULL;
SELECT * FROM users WHERE phone IS NOT NULL;

-- ORDER BY
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users ORDER BY country ASC, name ASC;
```

---

## Joins

Combine rows from multiple tables.

```sql
-- INNER JOIN (only matching rows)
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN (all rows from left table)
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN (all rows from right table)
SELECT u.name, o.total
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- FULL OUTER JOIN (all rows from both tables)
SELECT u.name, o.total
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;

-- Self join (join table to itself)
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Multiple joins
SELECT u.name, o.id AS order_id, p.name AS product
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

---

## Aggregation & Grouping

Summarize data with aggregate functions.

```sql
-- COUNT
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT country) FROM users;

-- SUM, AVG, MIN, MAX
SELECT SUM(total) FROM orders;
SELECT AVG(price) FROM products;
SELECT MIN(price), MAX(price) FROM products;

-- GROUP BY
SELECT country, COUNT(*) AS user_count
FROM users
GROUP BY country;

SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- HAVING (filter after grouping)
SELECT country, COUNT(*) AS user_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;

-- GROUP BY with multiple columns
SELECT country, city, COUNT(*) AS count
FROM users
GROUP BY country, city
ORDER BY count DESC;
```

---

## Data Manipulation (INSERT, UPDATE, DELETE)

Add, modify, and remove data.

```sql
-- INSERT single row
INSERT INTO users (name, email, created_at)
VALUES ('Alice', 'alice@example.com', NOW());

-- INSERT multiple rows
INSERT INTO products (name, price, category)
VALUES
  ('Widget A', 9.99, 'widgets'),
  ('Widget B', 14.99, 'widgets'),
  ('Gadget X', 49.99, 'gadgets');

-- INSERT from SELECT
INSERT INTO archived_orders (id, user_id, total)
SELECT id, user_id, total FROM orders WHERE created_at < '2023-01-01';

-- UPDATE rows
UPDATE users SET active = false WHERE last_login < '2023-01-01';

-- UPDATE multiple columns
UPDATE products
SET price = price * 1.1, updated_at = NOW()
WHERE category = 'electronics';

-- DELETE rows
DELETE FROM sessions WHERE expires_at < NOW();

-- DELETE all rows (keep table structure)
DELETE FROM temp_data;
-- or faster:
TRUNCATE TABLE temp_data;

-- UPSERT (INSERT or UPDATE on conflict) — PostgreSQL
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON CONFLICT (id) DO UPDATE
SET name = EXCLUDED.name, email = EXCLUDED.email;
```

---

## Data Definition (CREATE, ALTER, DROP)

Define and modify database schema.

```sql
-- Create a table
CREATE TABLE users (
  id          SERIAL PRIMARY KEY,
  name        VARCHAR(100) NOT NULL,
  email       VARCHAR(255) UNIQUE NOT NULL,
  age         INTEGER CHECK (age >= 0),
  role        VARCHAR(50) DEFAULT 'user',
  active      BOOLEAN DEFAULT true,
  created_at  TIMESTAMP DEFAULT NOW()
);

-- Create table with foreign key
CREATE TABLE orders (
  id         SERIAL PRIMARY KEY,
  user_id    INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  total      DECIMAL(10, 2) NOT NULL,
  status     VARCHAR(50) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW()
);

-- Add a column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Drop a column
ALTER TABLE users DROP COLUMN phone;

-- Rename a column
ALTER TABLE users RENAME COLUMN name TO full_name;

-- Change column type
ALTER TABLE users ALTER COLUMN age TYPE BIGINT;

-- Add a constraint
ALTER TABLE users ADD CONSTRAINT chk_age CHECK (age >= 18);

-- Drop a table
DROP TABLE temp_data;
DROP TABLE IF EXISTS temp_data;

-- Create a view
CREATE VIEW active_users AS
SELECT id, name, email FROM users WHERE active = true;
```

---

## Indexes & Constraints

Optimize queries and enforce data integrity.

```sql
-- Create an index
CREATE INDEX idx_users_email ON users(email);

-- Create a unique index
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Create a composite index
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Create a partial index
CREATE INDEX idx_active_users ON users(email) WHERE active = true;

-- Drop an index
DROP INDEX idx_users_email;

-- Common constraints
CREATE TABLE products (
  id       SERIAL PRIMARY KEY,           -- PRIMARY KEY
  sku      VARCHAR(50) UNIQUE NOT NULL,  -- UNIQUE + NOT NULL
  price    DECIMAL CHECK (price > 0),    -- CHECK
  category VARCHAR(50) DEFAULT 'misc'    -- DEFAULT
);
```

---

## Subqueries & CTEs

Write complex queries with nested logic.

```sql
-- Subquery in WHERE
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 1000);

-- Subquery in FROM (derived table)
SELECT avg_order.user_id, avg_order.avg_total
FROM (
  SELECT user_id, AVG(total) AS avg_total
  FROM orders
  GROUP BY user_id
) AS avg_order
WHERE avg_order.avg_total > 500;

-- Correlated subquery
SELECT name, email
FROM users u
WHERE EXISTS (
  SELECT 1 FROM orders o WHERE o.user_id = u.id
);

-- CTE (Common Table Expression)
WITH high_value_customers AS (
  SELECT user_id, SUM(total) AS lifetime_value
  FROM orders
  GROUP BY user_id
  HAVING SUM(total) > 5000
)
SELECT u.name, hvc.lifetime_value
FROM users u
JOIN high_value_customers hvc ON u.id = hvc.user_id
ORDER BY hvc.lifetime_value DESC;

-- Recursive CTE (e.g., org chart)
WITH RECURSIVE org_chart AS (
  SELECT id, name, manager_id, 0 AS level
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, oc.level + 1
  FROM employees e
  JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## Window Functions

Perform calculations across related rows without collapsing them.

```sql
-- ROW_NUMBER: assign sequential row numbers
SELECT name, salary,
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK and DENSE_RANK
SELECT name, department, salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- LAG and LEAD: access previous/next row values
SELECT date, revenue,
  LAG(revenue) OVER (ORDER BY date) AS prev_revenue,
  revenue - LAG(revenue) OVER (ORDER BY date) AS change
FROM daily_sales;

-- Running total (SUM as window function)
SELECT date, revenue,
  SUM(revenue) OVER (ORDER BY date) AS running_total
FROM daily_sales;

-- Partition by group
SELECT department, name, salary,
  AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;
```
