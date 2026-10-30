# Task 2 – Data Analysis and Visualization

**📌 Project Overview**

This project performs exploratory data analysis (EDA) on the Sample - Superstore dataset using Python. The notebook examines sales, profit, quantity, discount, categories, regions, customer segments, products, and time-based sales trends.

**🎯 Objectives**

* Load and inspect the Superstore dataset.
* Understand the dataset structure, columns, and data types.
* Check for missing values and duplicate records.
* Convert date columns into datetime format.
* Generate descriptive statistics for numerical variables.
* Analyze sales and profit across categories and regions.
* Study the relationship between discount and profit.
* Identify top products by sales and profit.
* Analyze monthly sales trends.
* Identify loss-making orders and category-wise losses.
* Use visualizations to communicate important patterns.

**🛠️ Technologies Used**

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab / Jupyter Notebook

**📂 Dataset**

**Dataset:** Sample - Superstore

The notebook loads the dataset using:

```python
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
```

The analysis uses fields such as:

* Order Date
* Ship Date
* Sales
* Quantity
* Discount
* Profit
* Category
* Region
* Segment
* Ship Mode
* Product Name

**🔎 Analysis Performed**

**1. Data Loading and Inspection**

The dataset is loaded into a Pandas DataFrame and inspected using:

```python
df.head()
df.shape
df.columns
df.info()
```

**2. Data Quality Checks**

The notebook checks:

* Missing values using `df.isnull().sum()`
* Duplicate records using `df.duplicated().sum()`

**3. Date Conversion**

The Order Date and Ship Date columns are converted to datetime format for time-based analysis.

**4. Descriptive Statistics**

Descriptive statistics are generated for the dataset and key numerical columns:

* Sales
* Profit
* Quantity
* Discount

**5. Category, Region, Segment and Ship Mode Analysis**

Value counts are used to understand the distribution of:

* Product categories
* Regions
* Customer segments
* Shipping modes

**6. Sales and Profit Visualization**

The notebook creates:

* Sales distribution histogram
* Profit distribution histogram
* Sales boxplot
* Total sales by category
* Total profit by category
* Total profit by region

**7. Correlation Analysis**

Correlation is calculated for:

* Sales
* Quantity
* Discount
* Profit

A correlation heatmap is used to visualize the relationships between these numerical variables.

**8. Monthly Sales Trend**

Monthly sales are calculated from the Order Date field and visualized using a line chart to understand sales patterns over time.

**9. Discount vs Profit**

A scatter plot is created to examine the relationship between discount and profit.

**10. Product Analysis**

The notebook identifies:

* Top 10 products by total sales
* Top 10 products by total profit

**11. Loss Analysis**

Orders with negative profit are identified. The notebook also calculates:

* Number of loss-making orders
* Total loss
* Loss by category

**📊 Visualizations Included**

* Distribution of Sales
* Distribution of Profit
* Boxplot of Sales
* Total Sales by Category
* Total Profit by Category
* Correlation Heatmap
* Monthly Sales Trend
* Total Profit by Region
* Discount vs Profit
* Top 10 Products by Sales
* Top 10 Products by Profit

**💡 Key Takeaways**

The notebook is designed to help understand overall business performance through sales and profit analysis. It highlights differences across product categories and regions, explores product-level performance, examines the impact of discounts on profit, identifies sales trends over time, and detects loss-making orders.

**Note:** Specific numerical findings are intentionally not listed here because the uploaded notebook contains the analysis code but does not contain executed cell outputs.

**🚀 How to Run**

**Google Colab**

1. Open the notebook in Google Colab.
2. Run the file-upload cell.
3. Upload `Sample - Superstore.csv`.
4. Run the cells from top to bottom.
5. Review the tables and visualizations.

**Local Jupyter Notebook**

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Place `Sample - Superstore.csv` in the same folder as the notebook and run the notebook cells sequentially.

**📁 Project Structure**

```text
Task-2/
│
├── Task_2.ipynb
├── Sample - Superstore.csv
└── README.md
```

**👩‍💻 Author**

**Mounika**

B.Tech – Data Science

**⭐ Skills Demonstrated**

Python • Pandas • NumPy • Data Cleaning • Exploratory Data Analysis • Data Visualization • Statistical Analysis
