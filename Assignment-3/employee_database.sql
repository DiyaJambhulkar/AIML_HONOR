CREATE DATABASE employee;

USE employee;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT
);

INSERT INTO employee VALUES
(101, 'Rahul', 'IT', 50000),
(102, 'Diya', 'CSE', 60000),
(103, 'Rutvik', 'Finance', 55000),
(104, 'Pavan', 'HR', 84000),
(105, 'Archana', 'Sales', 90000);

SELECT * FROM employee;