# Task-22-SQL-Filtering-Practice

Day 22 of 45 — Data Analytics Internship

Organization: Veda Technology
Internship: Data Analytics Intern
GitHub Repository Name: SQL-Filtering-Practice

Objective

Practice common SQL filtering techniques using the Northwind dataset.

Tools Used

•
MySQL

•
PostgreSQL

•
MySQL Workbench or PostgreSQL client

•
Northwind dataset

Concepts Covered

•
WHERE

•
IN

•
BETWEEN

•
NOT BETWEEN

•
LIKE

•
AND

•
ORDER BY

•
Ascending and descending sorting

Queries Included

The sql_filtering_practice.sql file contains 12 queries:

1.
Filter customers from the USA

2.
Filter customers from selected countries using IN

3.
Find products within a price range using BETWEEN

4.
Find products outside a price range using NOT BETWEEN

5.
Find products whose names begin with specific letters using LIKE

6.
Find companies containing a specific word using LIKE

7.
Filter customers from Brazil, France, or the UK

8.
Find cities beginning with the letter L

9.
Find high-priced active products

10.
Find contact names ending with specific letters

11.
Find tea products within a price range

12.
Filter customers from selected cities using IN

Deliverables

•
sql_filtering_practice.sql — 12 SQL queries with embedded expected result previews

•
README.md — Project documentation

How to Run

1.
Import the Northwind dataset into MySQL or PostgreSQL.

2.
Open sql_filtering_practice.sql.

3.
Run each query separately.

4.
Compare the actual results with the expected result previews included as comments.

Interview Notes

Difference Between LIKE and =

•
Use = for an exact match, such as:

SQL


WHERE Country = 'USA';



•
Use LIKE for pattern matching, such as:

SQL


WHERE ProductName LIKE 'Ch%';



The % wildcard represents zero or more characters.

When to Use BETWEEN

Use BETWEEN when filtering values within an inclusive range:

SQL


WHERE UnitPrice BETWEEN 20 AND 50;



This includes values equal to 20 and 50.

When to Use IN

Use IN when checking a column against multiple exact values:

SQL


WHERE Country IN ('USA', 'UK', 'Germany');



Author

Completed as part of the Veda Technology Data Analytics Internship.

