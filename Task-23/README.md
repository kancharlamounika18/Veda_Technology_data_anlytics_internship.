# Task-23-SQL-Aggregation-Basics
SQL Aggregation Basics

Day 23 of 45 — Data Analytics Internship

Organization: Veda Technology
Internship: Data Analytics Intern
GitHub Repository Name: SQL-Aggregation-Basics

Objective

Learn and practice SQL aggregate functions using the Northwind dataset.

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
COUNT()

•
SUM()

•
AVG()

•
MIN()

•
MAX()

•
GROUP BY

•
JOIN

•
Aggregate functions with grouped data

•
NULL behavior in aggregate functions

Queries Included

The sql_aggregation_basics.sql file contains 10 queries:

1.
Count the total number of customers

2.
Count the total number of products

3.
Calculate the total units in stock

4.
Calculate the average product price

5.
Find the minimum and maximum product prices

6.
Count customers by country

7.
Calculate product count and average price by category

8.
Group products by discontinued status

9.
Find the price range by supplier

10.
Calculate inventory value by category

Deliverables

•
sql_aggregation_basics.sql — 10 SQL aggregation queries with expected result previews

•
README.md — Project documentation

How to Run

1.
Import the Northwind dataset into MySQL or PostgreSQL.

2.
Open sql_aggregation_basics.sql.

3.
Run each query separately.

4.
Compare the query results with the expected result previews included as comments.

Interview Notes

Why Use GROUP BY?

GROUP BY combines rows with the same value so aggregate calculations can be performed for each group. For example, it can calculate the number of customers in each country.

How Do Aggregate Functions Handle NULL Values?

•
COUNT(*) counts all rows.

•
COUNT(column_name) ignores NULL values in that column.

•
AVG(), SUM(), MIN(), and MAX() generally ignore NULL values.

Dataset

This project uses the Northwind sample dataset, including customer, product, category, and supplier information.

Internship

Completed as part of the Veda Technology Data Analytics Internship.

