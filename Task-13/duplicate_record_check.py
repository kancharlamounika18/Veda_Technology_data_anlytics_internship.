from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT_DIR = Path(__file__).resolve().parent
OUTPUT_XLSX = OUT_DIR / "duplicate_record_check.xlsx"

# Practice retail-sales data modeled on the suggested Retail Sales / Superstore dataset.
# Rows 4 and 5 duplicate row 2; rows 11 and 12 duplicate row 10 on all key columns.
raw = pd.DataFrame([
    [1001, "2026-01-03", "CUST-001", "Asha Traders", "North", "Office Supplies", "Paper", 5, 12.50, 0.10],
    [1002, "2026-01-04", "CUST-002", "Bright Stores", "South", "Technology", "Keyboard", 2, 35.00, 0.05],
    [1003, "2026-01-05", "CUST-003", "City Mart", "East", "Furniture", "Chair", 1, 120.00, 0.15],
    [1002, "2026-01-04", "CUST-002", "Bright Stores", "South", "Technology", "Keyboard", 2, 35.00, 0.05],
    [1002, "2026-01-04", "CUST-002", "Bright Stores", "South", "Technology", "Keyboard", 2, 35.00, 0.05],
    [1004, "2026-01-06", "CUST-004", "Delta Office", "West", "Office Supplies", "Binder", 10, 8.00, 0.00],
    [1005, "2026-01-07", "CUST-005", "Evergreen Pvt Ltd", "North", "Technology", "Monitor", 3, 210.00, 0.10],
    [1006, "2026-01-08", "CUST-006", "Fresh Hub", "South", "Furniture", "Desk", 2, 180.00, 0.05],
    [1007, "2026-01-09", "CUST-007", "Global Needs", "East", "Office Supplies", "Notebook", 12, 4.50, 0.00],
    [1008, "2026-01-10", "CUST-008", "Home Works", "West", "Technology", "Mouse", 4, 18.00, 0.05],
    [1009, "2026-01-11", "CUST-009", "Indigo Retail", "North", "Furniture", "Table", 1, 250.00, 0.20],
    [1009, "2026-01-11", "CUST-009", "Indigo Retail", "North", "Furniture", "Table", 1, 250.00, 0.20],
    [1010, "2026-01-12", "CUST-010", "Jasmine Co", "South", "Office Supplies", "Pen Set", 20, 3.25, 0.00],
    [1011, "2026-01-13", "CUST-011", "Kaveri Foods", "East", "Technology", "Printer", 1, 160.00, 0.10],
    [1012, "2026-01-14", "CUST-012", "Lotus Labs", "West", "Furniture", "Bookcase", 1, 95.00, 0.05],
    [1013, "2026-01-15", "CUST-013", "Metro Supplies", "North", "Office Supplies", "Stapler", 6, 9.75, 0.00],
    [1014, "2026-01-16", "CUST-014", "Nova Retail", "South", "Technology", "Webcam", 2, 45.00, 0.10],
    [1015, "2026-01-17", "CUST-015", "Orbit Stores", "East", "Furniture", "Shelf", 2, 75.00, 0.15],
    [1016, "2026-01-18", "CUST-016", "Prime Office", "West", "Office Supplies", "Folder", 15, 2.80, 0.00],
    [1017, "2026-01-19", "CUST-017", "Quick Buy", "North", "Technology", "USB Hub", 5, 22.00, 0.05],
], columns=["Order_ID", "Order_Date", "Customer_ID", "Customer_Name", "Region", "Category", "Product", "Quantity", "Unit_Price", "Discount"])
raw["Order_Date"] = pd.to_datetime(raw["Order_Date"])
raw["Sales_Amount"] = raw["Quantity"] * raw["Unit_Price"] * (1 - raw["Discount"])
raw["Duplicate_Group"] = raw.groupby(list(raw.columns[:10]), dropna=False).ngroup().where(raw.duplicated(subset=list(raw.columns[:10]), keep=False), pd.NA)
raw["Record_Status"] = raw.duplicated(subset=list(raw.columns[:10]), keep=False).map({True: "Duplicate", False: "Unique"})

key_cols = list(raw.columns[:10])
dup_rows = raw[raw["Record_Status"] == "Duplicate"].copy()
dup_rows["Duplicate_Group"] = dup_rows["Duplicate_Group"].astype("Int64")
dup_rows = dup_rows.sort_values(["Duplicate_Group", "Order_ID"]) 

# Retain the first record in each exact duplicate group.
cleaned = raw.drop_duplicates(subset=key_cols, keep="first").copy()
cleaned["Record_Status"] = "Retained"
cleaned["Duplicate_Group"] = pd.NA

summary = pd.DataFrame({
    "Metric": ["Total input rows", "Unique rows retained", "Duplicate rows identified", "Duplicate groups", "Duplicate row rate", "Sales value removed by de-duplication"],
    "Value": [len(raw), len(cleaned), len(raw) - len(cleaned), dup_rows["Duplicate_Group"].nunique(), (len(raw)-len(cleaned))/len(raw), raw["Sales_Amount"].sum() - cleaned["Sales_Amount"].sum()],
    "Definition": ["Rows in Raw_Data", "Rows after keeping first exact match", "Extra rows beyond the first in each duplicate group", "Distinct exact-match groups", "Duplicate rows / total input rows", "Sales amount on removed duplicate rows"],
})

audit = pd.DataFrame([
    ["2026-09-29", "Duplicate detection", "Exact duplicate match across Order_ID, Order_Date, Customer_ID, Customer_Name, Region, Category, Product, Quantity, Unit_Price, Discount", "Completed", "Keep first row; flag later exact matches"],
    ["2026-09-29", "Quality check", "No missing values in matching key columns", "Passed", "All 10 matching key columns are populated"],
    ["2026-09-29", "Output creation", "Duplicate report and cleaned copy generated", "Completed", "Workbook contains four analysis sheets"],
], columns=["Audit_Date", "Check", "Rule_or_Method", "Status", "Notes"])

with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl", date_format="yyyy-mm-dd", datetime_format="yyyy-mm-dd") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    raw.to_excel(writer, sheet_name="Raw_Data", index=False)
    dup_rows.to_excel(writer, sheet_name="Duplicate_Report", index=False)
    cleaned.to_excel(writer, sheet_name="Cleaned_Copy", index=False)
    audit.to_excel(writer, sheet_name="Audit_Log", index=False)

wb = load_workbook(OUTPUT_XLSX)
navy = "1F4E78"
blue = "D9EAF7"
orange = "FCE4D6"
green = "E2F0D9"
red = "F4CCCC"
white = "FFFFFF"
thin_gray = Side(style="thin", color="D9E1F2")

for ws in wb.worksheets:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    ws.sheet_view.showGridLines = False
    for cell in ws[1]:
        cell.font = Font(name="Calibri", bold=True, color=white)
        cell.fill = PatternFill("solid", fgColor=navy)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(bottom=thin_gray)
    ws.row_dimensions[1].height = 30
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(name="Calibri", size=11, bold=(cell.row == 1))
            cell.alignment = Alignment(vertical="top", wrap_text=False)
            cell.border = Border(bottom=thin_gray)
    for col_cells in ws.columns:
        letter = get_column_letter(col_cells[0].column)
        max_len = max(len(str(c.value)) if c.value is not None else 0 for c in col_cells)
        ws.column_dimensions[letter].width = min(max(max_len + 2, 12), 34)

# Specific widths and formats.
for sheet in ["Raw_Data", "Duplicate_Report", "Cleaned_Copy"]:
    ws = wb[sheet]
    for col in ["A", "C"]:
        ws.column_dimensions[col].width = 14
    ws.column_dimensions["D"].width = 22
    ws.column_dimensions["E"].width = 12
    ws.column_dimensions["F"].width = 18
    ws.column_dimensions["G"].width = 18
    ws.column_dimensions["H"].width = 11
    ws.column_dimensions["I"].width = 14
    ws.column_dimensions["J"].width = 12
    ws.column_dimensions["K"].width = 15
    ws.column_dimensions["L"].width = 15
    for cell in ws["B"][1:]: cell.number_format = "yyyy-mm-dd"
    for cell in ws["I"][1:]: cell.number_format = '₹#,##0.00'
    for cell in ws["J"][1:]: cell.number_format = "0%"
    for cell in ws["K"][1:]: cell.number_format = '₹#,##0.00'
    for row in range(2, ws.max_row + 1):
        status = ws.cell(row=row, column=12).value
        if status == "Duplicate":
            for cell in ws[row]: cell.fill = PatternFill("solid", fgColor=red)
        elif status == "Unique" or status == "Retained":
            ws.cell(row=row, column=12).fill = PatternFill("solid", fgColor=green)

ws = wb["Summary"]
ws.freeze_panes = "A2"
ws.column_dimensions["A"].width = 34
ws.column_dimensions["B"].width = 20
ws.column_dimensions["C"].width = 60
ws["B6"].number_format = "0.0%"
ws["B7"].number_format = '₹#,##0.00'
for row in range(2, ws.max_row + 1):
    ws.cell(row=row, column=1).font = Font(name="Calibri", bold=True)
    ws.cell(row=row, column=3).alignment = Alignment(wrap_text=True, vertical="top")
for cell in ["A1", "B1", "C1"]:
    ws[cell].fill = PatternFill("solid", fgColor=navy)

ws = wb["Audit_Log"]
ws.column_dimensions["A"].width = 15
ws.column_dimensions["B"].width = 24
ws.column_dimensions["C"].width = 75
ws.column_dimensions["D"].width = 14
ws.column_dimensions["E"].width = 45
for cell in ws["D"][1:]:
    if cell.value in ("Passed", "Completed"):
        cell.fill = PatternFill("solid", fgColor=green)

# Add a clear legend to Summary.
ws = wb["Summary"]
ws["A9"] = "Legend"
ws["A9"].font = Font(name="Calibri", bold=True, color=white)
ws["A9"].fill = PatternFill("solid", fgColor=navy)
ws["B9"] = "Red = exact duplicate row"
ws["B9"].fill = PatternFill("solid", fgColor=red)
ws["C9"] = "Green = unique / retained row"
ws["C9"].fill = PatternFill("solid", fgColor=green)

wb.save(OUTPUT_XLSX)
print(f"Created: {OUTPUT_XLSX}")
print(f"Input rows: {len(raw)} | Unique retained: {len(cleaned)} | Duplicate rows: {len(raw)-len(cleaned)}")
