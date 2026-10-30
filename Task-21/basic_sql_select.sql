-- Basic SQL SELECT | Veda Technology Data Analytics Internship
-- Dataset: Northwind (MySQL/PostgreSQL-compatible table and column names)

-- Query 1
SELECT *
FROM Customers;

-- Query 2
SELECT CustomerID, CompanyName, Country
FROM Customers;

-- Query 3
SELECT CustomerID, CompanyName, Country
FROM Customers
WHERE Country = 'USA';

-- Query 4
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;

-- Query 5
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice < 20;

-- Query 6
SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice ASC;

-- Query 7
SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;

-- Query 8
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 20
ORDER BY UnitPrice DESC;

-- Query 9
SELECT CustomerID, CompanyName, City, Country
FROM Customers
WHERE Country = 'Germany'
ORDER BY CompanyName ASC;

-- Query 10
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice >= 20
AND UnitPrice <= 50
ORDER BY UnitPrice ASC;
