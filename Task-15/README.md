# Task-15-Product-Count-Analysis
Product Count Analysis

Veda Technology – Data Analytics Internship

Task Overview

This task focuses on analyzing the number of products in each product category using Microsoft Excel. The objective is to practice COUNTIF/COUNTIFS functions, identify unique products, and determine the category with the highest product count.

Objective

Count products by category.

Practice Excel COUNTIF/COUNTIFS functions.

Check unique Product IDs.

Identify the category with the largest number of products.

Present the results in a clear summary table.

Dataset

Dataset: Superstore_product_Dataset

Important columns used:

Product ID: Column N

Category: Column O

Common categories:

Furniture

Office Supplies

Technology

Tools Used

Microsoft Excel

Excel formulas

PivotTable (optional)

Methodology

1. Create a Product Count Analysis sheet

Create a new worksheet named:

Product Count Analysis

Create a summary table with:

Category

Product Count

Furniture



Office Supplies



Technology



2. Count product records by category

To count all records for each category, use:

=COUNTIF('Raw Data'!$O:$O,A2)

Copy the formula down for all categories.

3. Count unique products

Since the task asks to check unique products, use the Product ID column (N) and Category column (O).

For Excel versions supporting UNIQUE and FILTER:

=COUNTA(UNIQUE(FILTER('Raw Data'!$N$2:$N$9995,'Raw Data'!$O$2:$O$9995=A2)))

Replace 9995 with the actual last row of the dataset if necessary.

This counts distinct Product IDs belonging to the selected category.

4. Identify the largest category

Use:

=INDEX(A2:A4,MATCH(MAX(B2:B4),B2:B4,0))

This returns the category with the highest product count.

To find the highest count:

=MAX(B2:B4)

Deliverables

Product Count Analysis table

Unique product count by category

Largest/top category

Highest product count

Optional column chart: Product Count by Category

Expected Final Summary

Category

Unique Product Count

Furniture

Actual result

Office Supplies

Actual result

Technology

Actual result

Top Category: Actual result

Highest Product Count: Actual result

Optional PivotTable

A PivotTable can also be used:

Select the complete dataset.

Go to Insert → PivotTable.

Add Category to Rows.

Add Product ID to Values.

If available, select Distinct Count for Product ID.

Key Learning

This task demonstrates how Excel can be used to categorize and summarize product data efficiently. It also highlights the difference between counting records and counting unique products.

Conclusion

The Product Count Analysis provides a category-wise view of the Superstore product data and helps identify the category containing the highest number of unique products.

Internship: Veda Technology – Data Analytics
