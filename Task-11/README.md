# Veda Technology Internship - Data Analytics Track
## Basic Data Sorting and Filtering

**Intern Name:** Kancharla Mounika 
**Track:** Data Analytics  
**Company:** VEDA TECHNOLOGY  
**Focus:** Non-destructive data exploration, multi-criteria filtering, and business analysis  

---

### Project Overview

This repository contains the complete implementation for the Basic Data Sorting and Filtering assignment within the Veda Technology Internship Program. The primary objective is to demonstrate rigorous data exploration techniques by answering five specific business questions from a transactional retail dataset using multi-level sorting and filtering, while keeping the raw data completely intact.

---

### Repository Architecture

The project delivers an analysis workbook structured across seven dedicated sheets:

1. **Executive_Summary**: Master dashboard listing the five business questions, applied filter parameters, sorting directions, key operational findings, and responses to the technical interview questions.
2. **Q1_Top10_Tech_Profits**: Top 10 most profitable transactions in the Technology category (Category = 'Technology', Profit Descending).
3. **Q2_Consumer_Losses**: Multi-condition audit isolating Consumer orders with discounts >= 20% that resulted in financial losses (Segment = 'Consumer', Discount >= 0.20, Profit < 0, Profit Ascending).
4. **Q3_HighVol_West_Furniture**: Bulk orders of Furniture in the West region (Category = 'Furniture', Region = 'West', Quantity >= 8, Quantity Descending).
5. **Q4_OfficeSupplies_Subcats**: Aggregated revenue and margin breakdown for Office Supplies sub-categories, sorted by Total Revenue Descending.
6. **Q5_Q4_HighValue_Standard**: High-value transactions (Sales >= $1,000) during Q4 2024 routed via Standard Class delivery (Sales Descending).
7. **Raw_Data**: Preserved single source of truth containing 500 complete transactions with AutoFilter enabled, frozen header panes, and formatted numeric columns.

---

### Key Operational Findings

| # | Business Question | Filter Criteria | Sort Order | Finding |
| :--- | :--- | :--- | :--- | :--- |
| **Q1** | What are the top 10 most profitable transactions in Technology? | Category = 'Technology' | Profit Descending | Top 10 generated $7,133.00 profit; Apple iPhone 15 Pro led margins. |
| **Q2** | Which Consumer orders with >= 20% discount resulted in net losses? | Segment = 'Consumer' AND Discount >= 0.20 AND Profit < 0 | Profit Ascending | 21 deficit transactions identified, totaling $3,546.80 in losses. |
| **Q3** | What are the high-volume orders (Qty >= 8) for Furniture in the West? | Category = 'Furniture' AND Region = 'West' AND Quantity >= 8 | Quantity Descending | 15 bulk orders isolated, representing 134 total units. |
| **Q4** | How do Office Supplies sub-categories rank by sales volume and margin? | Category = 'Office Supplies' | Total Revenue Descending | Storage and Appliances generate the highest revenue, with margins > 28%. |
| **Q5** | Which high-value transactions (Sales >= $1,000) occurred in Q4 using Standard shipping? | Date in Q4 2024 AND Sales >= $1,000 AND Ship Mode = 'Standard Class' | Sales Descending | 22 orders isolated, delivering $41,250.40 in revenue with optimal logistics cost. |

---

### Technical Interview Questions

**Q1: When would you use filtering instead of deleting rows?**  
Filtering must be used in exploratory and operational analyses whenever source records are evaluated. It preserves complete data integrity, keeps relational dependencies and formulas intact, enables rapid pivoting across different segments without data loss, and guarantees an auditable trace. Deleting rows permanently destroys historical context and cannot be reversed once saved.

**Q2: Why should raw data be preserved?**  
Raw data is the Single Source of Truth (SSOT). Preserving raw data guarantees reproducibility, supports multi-department usage from a common baseline, allows transformations to be re-run whenever business rules change, and complies with financial and regulatory audit requirements.

---

### Project File Structure

```
.
├── data/
│   └── superstore_retail_sales.csv
├── src/
│   ├── prepare_data.py
│   ├── generate_excel.py
│   └── generate_pdf_report.py
├── output/
│   ├── Superstore_Filtered_Analysis.xlsx
│
│  
├── README.md
├── README_FR.md
├── linkedin_post.txt
├── linkedin_post_FR.txt
└── requirements.txt
```

---

### Execution Instructions

```bash
pip install -r requirements.txt
python src/prepare_data.py
python src/generate_excel.py
python src/generate_pdf_report.py
```
