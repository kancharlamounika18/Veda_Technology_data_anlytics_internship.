# Task-13-Duplicate-Record-Check
Duplicate Record Check

📌 Task Overview

Task: Duplicate Record Check
Track: Data Analytics
Purpose: Find duplicate records in a dataset and document them
clearly.

🎯 Objective

The objective of this task is to understand how duplicate records can be
detected, reviewed, documented, and removed from a dataset.

🛠️ Tools Used

Microsoft Excel

Python

Pandas

📂 Suggested Datasets

You can use any suitable dataset, such as:

Retail Sales dataset

Superstore dataset

🔎 What is a Duplicate Record?

A duplicate record is a row that appears more than once in a dataset
with the same values across all columns or across the important key
columns.

For example:

Customer ID   Product     Sales

C001          Laptop      50000
C002          Mouse        1000
C001          Laptop      50000

The third row is a duplicate of the first row.

📝 Steps Performed

1. Load the Dataset

Open the dataset in Excel or load it using Pandas.

import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.head())

2. Check the Dataset Size

print(df.shape)

This shows the number of rows and columns.

3. Find Duplicate Rows

duplicates = df[df.duplicated()]
print(duplicates)

4. Count Duplicate Rows

duplicate_count = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)

5. Check Duplicates Using Key Columns

If duplicates need to be checked using specific columns:

duplicates = df[df.duplicated(
    subset=["Customer ID", "Product"],
    keep=False
)]

print(duplicates)

Replace the column names with the columns available in your dataset.

6. Create a Duplicate Report

Document the duplicate records separately. The report can contain:

Duplicate row number

Key column values

Duplicate values

Number of occurrences

Action taken

7. Remove Duplicate Records

After checking the duplicate records:

cleaned_df = df.drop_duplicates()

8. Validate the Cleaned Dataset

Check the duplicate count again:

print("Duplicates after cleaning:", cleaned_df.duplicated().sum())

The expected result should be:

Duplicates after cleaning: 0

if all exact duplicates were removed.

9. Save the Cleaned Dataset

cleaned_df.to_csv("cleaned_dataset.csv", index=False)

📦 Deliverables

This task should contain:

Duplicate Report -- records identified as duplicates.

Cleaned Copy -- dataset after duplicate records have been
handled.

Audit Note -- short documentation explaining what was checked
and what action was taken.

📋 Audit Note Example

The dataset was checked for duplicate records using full-row matching
and relevant key columns. Duplicate records were documented in a
separate duplicate report. After reviewing the duplicates, the
required duplicate rows were removed and the cleaned dataset was
validated again.

📊 Excel Method

In Excel, duplicate records can be checked using:

Data → Remove Duplicates

Before removing duplicates:

Keep a copy of the original dataset.

Identify the columns that define a duplicate.

Review the duplicate rows.

Document the duplicates.

Remove duplicates only after verification.

Save the cleaned dataset separately.

💡 Important Points

Always keep the original dataset unchanged.

Do not remove records without checking whether they are genuine
duplicates.

Check full rows as well as important key columns.

Keep an audit note of the cleaning process.

Validate the final dataset after removing duplicates.

🎤 Interview Questions

1. What is a duplicate row?

A duplicate row is a record that repeats an existing record based on the
columns being checked.

2. How can duplicates affect analysis?

Duplicates can increase counts, totals, averages, and other calculated
metrics, which can lead to incorrect analysis.

3. How do you find duplicates using Pandas?

Use the duplicated() method.

df.duplicated()

4. How do you remove duplicates using Pandas?

Use:

df.drop_duplicates()

5. Why should you keep an original copy?

Keeping the original dataset allows you to compare the cleaned data with
the source data and recover information if needed.

📁 Suggested Project Structure

Duplicate-Record-Check/
│
├── README.md
├── duplicate_record_check.py
├── duplicate_record_check.xlsx
└── retail_sales_input_dataset.csv

✅ Final Checklist

Dataset loaded

Dataset size checked

Duplicate records identified

Duplicate report created

Original dataset preserved

Duplicates reviewed

Cleaned dataset created

Duplicate count validated

Audit note documented

Files organized for submission

Data Analytics Internship Task -- Duplicate Record Check
