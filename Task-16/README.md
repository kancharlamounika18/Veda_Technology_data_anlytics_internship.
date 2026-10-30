# Task-16-simple-profit-analysis
Simple Profit Analysis

An Excel-based data analytics project that compares sales and profitability across product categories using the public Sample Superstore dataset.

Project Overview

This project was created for the Veda Technology Data Analytics internship task.

Objective

Understand basic profitability by comparing total sales, total profit, profit margins, and average performance across product categories.

Tools Used

•
Microsoft Excel / WPS Office / LibreOffice

•
Python and openpyxl for workbook preparation

•
Public Sample Superstore dataset

Repository Contents

File
Description
Simple_Profit_Analysis.xlsx
Completed Excel workbook containing the analysis, formulas, charts, and raw data.
Superstore_sales_dataset.csv
Source transaction-level dataset used for the analysis.
Submission_Notes.md
Key findings and interview-ready explanations.




Workbook Structure

Read Me

Contains the project brief, instructions, methodology, source information, and explanation of each worksheet.

Profit Summary

Contains:

•
Total sales

•
Total profit

•
Overall profit margin

•
Transaction count

•
Category-level sales and profit summary

•
Average sales and average profit

•
Profit ranking by category

•
Total Profit by Category chart

•
Sales vs Profit comparison chart

•
Interview questions and key takeaways

Raw Data

Contains 9,994 Superstore transaction records with fields such as:

•
Order date

•
Customer and segment

•
Region and state

•
Product category and sub-category

•
Sales

•
Quantity

•
Discount

•
Profit

Key Findings

Category
Total Sales
Total Profit
Profit Margin
Furniture
$741,999.80
$18,451.27
2.5%
Office Supplies
$719,047.03
$122,490.80
17.0%
Technology
$836,154.03
$145,454.95
17.4%
Overall
$2,297,200.86
$286,397.02
12.5%




Main Conclusion

Technology has the highest total sales and total profit. Furniture has substantial sales but a much lower profit margin, showing why revenue should not be evaluated without considering profitability.

Interview Questions

What is the difference between revenue and profit?

Revenue is the total amount generated from sales. Profit is the amount remaining after deducting costs, discounts, and other expenses. A business can have high revenue but low profit if its costs are high.

Why can sales be high but profit low?

Possible reasons include:

•
Heavy discounting

•
High product or operating costs

•
Product returns

•
Shipping and fulfillment costs

•
Low-margin products

•
An unfavorable product mix

Methodology

The Profit Summary worksheet uses Excel formulas including:

•
SUMIF for category-level sales and profit

•
AVERAGEIF for average category performance

•
COUNTIF for transaction counts

•
RANK for category profitability ranking

•
IFERROR for safe margin calculations

The workbook is designed to remain refreshable when the underlying raw data is updated.

Data Source

The project uses the public Sample Superstore transaction dataset, downloaded from a public GitHub mirror of the commonly used Tableau Superstore dataset.

How to Use

1.
Download Simple_Profit_Analysis.xlsx.

2.
Open it in Microsoft Excel, WPS Office, or LibreOffice.

3.
Open the Profit Summary worksheet to review the analysis and charts.

4.
Open Raw Data to filter or inspect transaction records.

5.
If new records are added, recalculate the workbook to refresh the formulas and charts.


