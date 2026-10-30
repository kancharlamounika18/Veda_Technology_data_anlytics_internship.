# Task-20-customer-order-count
Veda Technology — Data Analytics Day 20

Customer Order Count Analysis

This project is part of my Veda Technology Data Analytics Internship and my 45 Days of Data Analytics Learning Journey.

The objective of this task is to count distinct orders for each customer and identify frequent buyers while avoiding duplicate order lines.

Task Objective

Analyze customer purchasing behavior by:

•
Counting the number of distinct orders per customer

•
Avoiding duplicate product lines belonging to the same order

•
Ranking customers by order count

•
Identifying the top 10 frequent buyers

•
Demonstrating the analysis using Excel and SQL

Dataset

The project uses a Global Superstore-style retail dataset containing order, customer, product, sales, and shipping information.

Important columns used in the analysis:

•
Order ID

•
Customer ID

•
Customer Name

•
Order Date

•
Sales

Source dataset:

[Global Superstore Dataset](

https://github.com/yannie28/Global-Superstore/blob/master/Global_Superstore(CSV ).csv)

Important Data-Cleaning Rule

A single order can contain multiple product lines. Therefore, counting rows would overstate the number of orders.

For example:

Customer ID
Order ID
Product Lines
CG-12520
CA-100111
3




This represents one order, not three orders.

The correct approach is to count each unique combination of:

Plain Text


Customer ID + Order ID



In SQL, this is handled using:

SQL


COUNT(DISTINCT Order_ID)



Project Files

customer_order_count_analysis.xlsx
superstore.csv




Excel Workbook Sheets

1. Original Data

Contains the original Superstore order-line data.

2. Customer Orders

Contains unique customer-order combinations after removing duplicate product/order lines.

3. Customer Order Analysis

Contains:

•
Customer ID

•
Customer Name

•
Distinct Order Count

•
Customer ranking

•
Top 10 customer table

•
Summary metrics

•
Top 10 customers bar chart

SQL Analysis

Customer Order Count

SQL


SELECT
    Customer_ID,
    MAX(Customer_Name) AS Customer_Name,
    COUNT(DISTINCT Order_ID) AS Order_Count
FROM Superstore
GROUP BY Customer_ID
ORDER BY Order_Count DESC, Customer_ID;



Top 10 Customers

SQL


SELECT
    Customer_ID,
    MAX(Customer_Name) AS Customer_Name,
    COUNT(DISTINCT Order_ID) AS Order_Count
FROM Superstore
GROUP BY Customer_ID
ORDER BY Order_Count DESC, Customer_ID
LIMIT 10;



SQL Server Version

SQL


SELECT TOP 10
    Customer_ID,
    MAX(Customer_Name) AS Customer_Name,
    COUNT(DISTINCT Order_ID) AS Order_Count
FROM Superstore
GROUP BY Customer_ID
ORDER BY Order_Count DESC, Customer_ID;



Results Summary

•
Source rows analyzed: 1,000

•
Unique customer-order pairs: 867

•
Unique customers: 800

•
Maximum orders by one customer: 5

Tools Used

•
Microsoft Excel

•
Pivot Tables

•
SQL

•
Data Cleaning

•
Data Analysis

•
Data Visualization

Key Learning

The most important learning from this task is that order lines are not the same as orders. A customer may have several product rows under one Order ID, so distinct orders must be counted using the unique Order ID rather than the total number of rows.

