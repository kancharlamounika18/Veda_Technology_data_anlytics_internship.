-- SQL AGGREGATION BASICS | DAY 23 OF 45
-- Veda Technology – Data Analytics Internship
-- GitHub repository name: SQL-Aggregation-Basics
-- Dataset: Northwind
-- Topics: COUNT, SUM, AVG, MIN, MAX, GROUP BY, JOIN
--
-- Run each query separately in MySQL or PostgreSQL.
-- Expected result previews are included below as SQL comments.

-- ============================================================================
-- QUERY 1: Total number of customers
-- ============================================================================
SELECT COUNT(*) AS TotalCustomers
FROM Customers;

-- Expected result preview (1 of 1 row(s)):
-- TotalCustomers
-- 91

-- ============================================================================
-- QUERY 2: Total number of products
-- ============================================================================
SELECT COUNT(*) AS TotalProducts
FROM Products;

-- Expected result preview (1 of 1 row(s)):
-- TotalProducts
-- 77

-- ============================================================================
-- QUERY 3: Total units in stock
-- ============================================================================
SELECT SUM(UnitsInStock) AS TotalUnitsInStock
FROM Products;

-- Expected result preview (1 of 1 row(s)):
-- TotalUnitsInStock
-- 3119

-- ============================================================================
-- QUERY 4: Average product price
-- ============================================================================
SELECT AVG(UnitPrice) AS AverageUnitPrice
FROM Products;

-- Expected result preview (1 of 1 row(s)):
-- AverageUnitPrice
-- 28.83

-- ============================================================================
-- QUERY 5: Minimum and maximum product price
-- ============================================================================
SELECT MIN(UnitPrice) AS MinimumPrice, MAX(UnitPrice) AS MaximumPrice
FROM Products;

-- Expected result preview (1 of 1 row(s)):
-- MinimumPrice | MaximumPrice
-- 2.50 | 263.50

-- ============================================================================
-- QUERY 6: Customers by country
-- ============================================================================
SELECT Country, COUNT(*) AS CustomerCount
FROM Customers
GROUP BY Country
ORDER BY CustomerCount DESC;

-- Expected result preview (12 of 21 row(s)):
-- Country | CustomerCount
-- USA | 13
-- France | 11
-- Germany | 11
-- Brazil | 9
-- UK | 7
-- Mexico | 5
-- Spain | 5
-- Venezuela | 4
-- Argentina | 3
-- Canada | 3
-- Italy | 3
-- Austria | 2
-- ... 9 additional row(s)

-- ============================================================================
-- QUERY 7: Product count and average price by category
-- ============================================================================
SELECT c.CategoryName, COUNT(p.ProductID) AS ProductCount, AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY AveragePrice DESC;

-- Expected result preview (8 of 8 row(s)):
-- CategoryName | ProductCount | AveragePrice
-- Meat/Poultry | 6 | 54.01
-- Beverages | 12 | 37.98
-- Produce | 5 | 32.37
-- Dairy Products | 10 | 28.73
-- Confections | 13 | 25.16
-- Condiments | 12 | 22.85
-- Seafood | 12 | 20.68
-- Grains/Cereals | 7 | 20.25

-- ============================================================================
-- QUERY 8: Products by discontinued status
-- ============================================================================
SELECT Discontinued, COUNT(*) AS ProductCount, AVG(UnitPrice) AS AveragePrice
FROM Products
GROUP BY Discontinued;

-- Expected result preview (2 of 2 row(s)):
-- Discontinued | ProductCount | AveragePrice
-- 0 | 67 | 26.94
-- 1 | 10 | 41.50

-- ============================================================================
-- QUERY 9: Price range by supplier
-- ============================================================================
SELECT SupplierID, COUNT(*) AS ProductCount, MIN(UnitPrice) AS MinimumPrice, MAX(UnitPrice) AS MaximumPrice
FROM Products
GROUP BY SupplierID
ORDER BY SupplierID;

-- Expected result preview (12 of 29 row(s)):
-- SupplierID | ProductCount | MinimumPrice | MaximumPrice
-- 1 | 2 | 10 | 19
-- 2 | 4 | 17 | 22
-- 3 | 3 | 25 | 40
-- 4 | 3 | 10 | 97
-- 5 | 2 | 21 | 38
-- 6 | 3 | 6 | 23.25
-- 7 | 5 | 15 | 62.50
-- 8 | 5 | 9.20 | 81
-- 9 | 2 | 9 | 21
-- 10 | 1 | 4.50 | 4.50
-- 11 | 3 | 14 | 43.90
-- 12 | 5 | 7.75 | 123.79
-- ... 17 additional row(s)

-- ============================================================================
-- QUERY 10: Inventory value by category
-- ============================================================================
SELECT c.CategoryName, SUM(p.UnitPrice * p.UnitsInStock) AS InventoryValue
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY InventoryValue DESC;

-- Expected result preview (8 of 8 row(s)):
-- CategoryName | InventoryValue
-- Seafood | 13010.35
-- Beverages | 12480.25
-- Condiments | 11926.05
-- Dairy Products | 11271.20
-- Confections | 10392.20
-- Meat/Poultry | 5729.45
-- Grains/Cereals | 5594.50
-- Produce | 3549.35
-- ============================================================================
-- INTERVIEW NOTES
-- ============================================================================
-- GROUP BY combines rows with the same value so aggregate functions can be
-- calculated for each group, such as customers per country.
-- AVG ignores NULL values. COUNT(*) counts rows, while COUNT(column) ignores
-- NULL values in that column.
-- SUM, MIN, and MAX also ignore NULL values.
