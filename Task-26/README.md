# Task-26-Text-Cleaning-Basics

Day 26 of 45 — Data Science Internship

Organization: Veda Technology
Internship: Data Science Intern
GitHub Repository Name: Text-Cleaning-Basics

Objective

Standardize customer names, spaces, capitalization, email addresses, cities, and phone numbers using Python and Excel.

Tools Used

•
Python

•
pandas

•
Microsoft Excel

Project Files

•
customer_dataset.csv — Original customer dataset containing inconsistent text values

•
cleaned_customer_dataset.csv — Standardized customer dataset

•
text_cleaning.py — Reusable Python text-cleaning script

•
before_after_examples.xlsx — Before-and-after comparison workbook

Cleaning Operations

The project performs the following operations:

•
Removes leading and trailing whitespace

•
Collapses repeated spaces

•
Applies proper capitalization to customer names

•
Converts email addresses to lowercase

•
Removes spaces from email addresses

•
Standardizes city names

•
Keeps digits only in phone numbers

Excel Workbook Sheets

The before_after_examples.xlsx file contains:

•
Before_After — Raw and cleaned values side by side

•
Cleaning_Rules — Cleaning rules with examples

•
Summary — Project details and quality summary

How to Run

1.
Download all project files into the same folder.

2.
Make sure Python and pandas are installed.

3.
Open a terminal in the project folder.

4.
Run:

Bash


python text_cleaning.py



1.
The script reads customer_dataset.csv and creates cleaned_customer_dataset.csv.

2.
Open before_after_examples.xlsx to review the transformations.

Input and Output

The input file contains intentionally inconsistent values such as extra spaces, mixed capitalization, spaces inside email addresses, and formatted phone numbers. The output file contains standardized values suitable for further analysis.

Internship

Completed as part of the Veda Technology Data Science Internship.

