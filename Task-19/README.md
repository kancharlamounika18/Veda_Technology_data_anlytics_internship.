# Task-19-top10-superstore-sales-analysis
Top 10 Products by Sales — Superstore Task

Task

Identify the top 10 products by total sales from the Superstore dataset.

•
Objective: Practice ranking and sorting.

•
Tools: Excel and Python.

•
Deliverables: Top-10 table and chart.

•
Tie handling: If two products have the same total sales, products are ordered alphabetically by product name.

Dataset

This project uses the public Tableau Sample Superstore CSV dataset:

•
Source: 

Sample Superstore CSV on GitHub

•
Local file: superstore.csv

•
Important columns: Product Name and Sales

•
The source dataset contains order-level sales records; the analysis sums Sales for each product.

Files

File
Purpose
superstore.csv
Source dataset used for the analysis
top10_products.xlsx
Excel workbook with Top 10 summary/chart and Data sheet
top10_products_analysis.py
Reusable Python script
README.md
Instructions and explanation




Excel workbook

Open top10_products.xlsx in Excel, LibreOffice Calc, or WPS Office.

•
Top 10 sheet: ranked table and horizontal bar chart.

•
Data sheet: complete source data in a formatted table.

•
The sales cells in the Top-10 table use SUMIF formulas against the Data sheet.

Run the Python solution

From this folder:

Bash


python top10_products_analysis.py superstore.csv top10_products.xlsx



The script will:

1.
Load the CSV with pandas.

2.
Group rows by Product Name.

3.
Sum Sales for each product.

4.
Sort sales from highest to lowest.

5.
Keep the first 10 products.

6.
Print the results.

7.
Create the Excel workbook with a table, raw data, and chart.

Expected result

The generated workbook should show these products at the top when using this dataset:

1.
Canon imageCLASS 2200 Advanced Copier

2.
Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind

3.
Cisco TelePresence System EX90 Videoconferencing Unit

4.
HON 5400 Series Task Chairs for Big and Tall

5.
GBC DocuBind TL300 Electric Binding System

6.
GBC Ibimaster 500 Manual ProClick Binding System

7.
Hewlett Packard LaserJet 3310 Copier

8.
HP Designjet T520 Inkjet Large Format Printer - 24" Color

9.
GBC DocuBind P400 Electric Binding System

10.
High Speed Automatic Electric Letter Opener

The exact totals are calculated from the CSV by the workbook formulas and Python script.

Simple explanation

The main calculation is:

Plain Text


Total Sales per Product = sum of Sales for all rows with the same Product Name



Then the products are sorted in descending order and the first 10 rows are reported.

