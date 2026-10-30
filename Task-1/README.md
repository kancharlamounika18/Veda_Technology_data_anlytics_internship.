🛒 Superstore Data Cleaning & Preprocessing

A Python-based data cleaning and preprocessing project using the Superstore dataset. The project focuses on identifying data quality issues, handling missing values, checking data types, removing inconsistencies, and preparing a clean dataset for further analysis.

📌 Project Overview

Data cleaning is an important step in the Data Science workflow because raw datasets may contain missing values, duplicate records, incorrect data types, inconsistent formats, and other data quality issues.

In this project, the Superstore dataset is analyzed and cleaned using Python and Pandas. The cleaned dataset is then saved as a separate CSV file for future analysis and visualization.

🎯 Objectives

Understand the structure of the Superstore dataset

Inspect rows, columns, and data types

Identify missing values

Check for duplicate records

Detect inconsistent or invalid data

Clean and preprocess the dataset

Save the cleaned dataset for further analysis

Prepare the data for future Data Science and visualization tasks

📂 Dataset

The project uses the Sample Superstore dataset containing information related to orders, customers, products, sales, discounts, profits, and regions.

Dataset Statistics

Rows: 9,994

Columns: 21

Major Features

Feature

Description

Row ID

Unique identifier for each row

Order ID

Unique order identifier

Order Date

Date on which the order was placed

Ship Date

Date on which the order was shipped

Ship Mode

Shipping method

Customer ID

Unique customer identifier

Customer Name

Customer name

Segment

Customer segment

Country

Country of the customer

City

City of the customer

State

State of the customer

Postal Code

Postal code

Region

Geographical region

Product ID

Unique product identifier

Category

Product category

Sub-Category

Product sub-category

Product Name

Name of the product

Sales

Sales amount

Quantity

Quantity ordered

Discount

Discount applied

Profit

Profit generated

🛠️ Technologies Used

Python

Pandas

NumPy

Google Colab

Jupyter Notebook

🔍 Data Cleaning Process

The following steps are performed in the notebook:

1. Import Required Libraries

import pandas as pd
import numpy as np

2. Load the Dataset

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

3. Check Dataset Shape

print(df.shape)

Output:

(9994, 21)

This confirms that the dataset contains 9,994 records and 21 columns.

4. Display Dataset Information

df.info()

This step is used to understand the column names, data types, number of non-null values, and memory usage of the dataset.

5. Display the First Few Records

df.head()

This helps to understand the structure and contents of the dataset.

6. Check Missing Values

df.isnull().sum()

This step identifies the number of missing values present in each column.

7. Check Duplicate Records

df.duplicated().sum()

Duplicate records are identified to maintain data accuracy and consistency.

8. Remove Duplicate Records

df = df.drop_duplicates()

Duplicate rows can be removed to ensure that each record is unique.

9. Check Data Types

df.dtypes

This step verifies whether each column has the appropriate data type.

10. Convert Date Columns

Date columns can be converted into the proper datetime format for further analysis.

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

11. Check Unique Values

df.nunique()

This helps identify the number of unique values in each column and can be useful for detecting inconsistencies.

12. Check Numerical Summary

df.describe()

This provides statistical information such as count, mean, standard deviation, minimum, maximum, and quartile values for numerical columns.

13. Clean the Dataset

The dataset is processed by handling missing values, duplicate records, incorrect data types, and inconsistent values where required.

The cleaned dataset is then stored in a separate DataFrame.

14. Save the Cleaned Dataset

df.to_csv("cleaned_superstore.csv", index=False)

The cleaned dataset is saved as:

cleaned_superstore.csv

📁 Project Structure

Superstore-Data-Cleaning-Analysis/
│
├── Task-1.ipynb
├── Sample - Superstore.csv
├── cleaned_superstore.csv
└── README.md

📓 Project Files

Task-1.ipynb

Contains the complete Python implementation for:

Data loading

Data exploration

Data inspection

Missing value checking

Duplicate detection

Data type checking

Data cleaning

Dataset preprocessing

Exporting the cleaned dataset

Sample - Superstore.csv

The original Superstore dataset used for the project.

cleaned_superstore.csv

The processed and cleaned version of the original dataset.

📊 Dataset Information

The Superstore dataset contains business-related information about customer orders and products.

It includes:

Customer details

Order details

Shipping information

Product information

Sales

Quantity

Discounts

Profit

Geographical information

🎯 Key Learning Outcomes

Through this project, I gained practical experience in:

Loading CSV datasets using Pandas

Understanding DataFrame structure

Inspecting data types

Identifying missing values

Detecting duplicate records

Cleaning and preprocessing data

Converting data types

Performing basic statistical analysis

Exporting cleaned datasets

Preparing data for further analysis

🚀 How to Run the Project

Using Google Colab

Open Task-1.ipynb in Google Colab.

Upload Sample - Superstore.csv.

Run the notebook cells sequentially.

Perform the data cleaning operations.

Generate cleaned_superstore.csv.

Using Jupyter Notebook

Install the required libraries:

pip install pandas numpy jupyter

Open Jupyter Notebook:

jupyter notebook

Then open:

Task-1.ipynb

Run all the cells to reproduce the data cleaning process.

📈 Future Scope

The cleaned dataset can be further used for:

Exploratory Data Analysis (EDA)

Sales analysis

Profit analysis

Customer segmentation

Product performance analysis

Regional analysis

Data visualization

Business intelligence dashboards

Machine Learning projects

👩‍💻 Author

Kancharla Mounika

B.Tech – Data Science

Interested in Data Science, Machine Learning, Data Analytics, and Python.

⭐ Conclusion

This project demonstrates the importance of data cleaning and preprocessing in the Data Science workflow. By cleaning and preparing the Superstore dataset using Python and Pandas, the data becomes more reliable and suitable for further analysis, visualization, and machine learning applications.
