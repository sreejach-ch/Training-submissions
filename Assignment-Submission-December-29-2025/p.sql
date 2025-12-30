-- Customers table
CREATE TABLE customers (customer_id INTEGER, name TEXT);
-- Orders table
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    amount INTEGER
);
-- Employees table
CREATE TABLE employees (
    emp_id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);
-- Departments table
CREATE TABLE departments (
    dept_id INTEGER,
    dept_name TEXT,
    manager_id INTEGER
);
INSERT INTO customers
VALUES (1, 'Alice'),
    (2, 'Bob');
INSERT INTO orders
VALUES (101, 1, 250),
    (102, 2, 400);
INSERT INTO employees
VALUES (1, 'Alice', 'IT', 90000),
    (2, 'Bob', 'HR', 60000),
    (3, 'Charlie', 'IT', 75000);
INSERT INTO departments
VALUES (1, 'IT', 1),
    (2, 'HR', 2);