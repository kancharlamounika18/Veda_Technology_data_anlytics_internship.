# Task-12-Missing-Value-Identification
Missing Value Identification

Project Overview

This project is part of my Data Analytics Internship at Veda Technology.

The objective is to identify missing values in a dataset and summarize where they occur. This task focuses on basic missing-data inspection using Excel, Python, and Pandas.

Objective

Identify missing/null values in a dataset.

Count missing values column-wise.

Summarize where missing values occur.

Understand the importance of checking missing data before analysis.

Avoid removing data without proper justification.

Tools Used

Excel

Python

Pandas

Suggested Datasets

Titanic

Iris

Task Description

The task involves inspecting the selected dataset and identifying missing values.

Steps

Load the dataset.

Inspect the dataset structure.

Check for missing/null values.

Count missing values for each column.

Identify columns containing missing values.

Summarize the findings.

Do not remove rows or columns without proper justification.

Python Implementation

import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.isnull().sum())

To display only columns that contain missing values:

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

Expected Deliverables

Missing-value summary

Short findings/observations

Dataset inspection using Excel and/or Python with Pandas

Key Learning

Missing-value identification is an important data preprocessing step. Before deleting or replacing missing values, it is necessary to understand which columns contain missing values, how many values are missing, and how those missing values may affect the analysis.

Interview Questions

What is a missing value?

A missing value is a data point for which no value has been recorded in a dataset.

Why can blindly deleting rows be risky?

Deleting rows without understanding why values are missing can remove useful information and reduce the size and quality of the dataset.

Suggested Project Structure

Missing-Value-Identification/
│
├── dataset.csv
├── Missing_Value_Identification.py
├── missing_value_summary.csv
└── README.md

File names can be changed according to the actual files used for the task.

Internship

Data Analytics Internship — Veda Technology

This task helped strengthen my understanding of data-quality inspection and missing-value analysis using Excel, Python, and Pandas.

Disclaimer

This README documents an academic/internship learning task and its implementation approach.
