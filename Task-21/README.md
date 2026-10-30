# Basic SQL SELECT

## Internship
Veda Technology – Data Analytics Internship

## Objective
To understand and practice basic SQL `SELECT` queries using the Northwind dataset.

## Tools Used
- MySQL / PostgreSQL syntax
- MySQL Workbench-compatible query format
- Northwind dataset

## Concepts Covered
- `SELECT`
- `WHERE`
- `AND`
- `ORDER BY`
- `ASC` and `DESC`
- Filtering data
- Sorting data

## Queries Performed
1. Display all customers
2. Select specific customer columns
3. Filter customers by country (USA)
4. Find products above a specific price
5. Find products below a specific price
6. Sort products by price ascending
7. Sort products by price descending
8. Filter and sort products
9. Filter German customers alphabetically
10. Filter products within a price range

## Deliverables
- `basic_sql_select.sql` — ten SQL queries
- `outputs/query1_output.png` through `outputs/query10_output.png` — query result captures
- This README documentation

## Dataset Notes
The output images were generated from the standard Northwind sample dataset. The source schema uses lowercase snake_case names; for this task, the query examples use the requested readable names such as `Customers.CustomerID` and `Products.UnitPrice`. If your imported database uses lowercase names, adjust identifiers to match your local schema.

## How to Run
1. Create or select your database.
2. Import the Northwind dataset.
3. Open `basic_sql_select.sql` in MySQL Workbench or PostgreSQL.
4. Run each query and compare the result with the matching image in `outputs/`.
