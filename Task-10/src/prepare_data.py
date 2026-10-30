import csv
import random
from datetime import date, timedelta
import os

random.seed(42)

products = [
    ("Staples",           "Office Supplies", 2.99,  1.20),
    ("Binders",           "Office Supplies", 7.49,  2.80),
    ("Paper",             "Office Supplies", 19.99, 7.50),
    ("Pens",              "Office Supplies", 5.99,  1.90),
    ("Desk Lamp",         "Furniture",       45.00, 18.00),
    ("Bookcase",          "Furniture",       150.00, 62.00),
    ("Chair",             "Furniture",       229.99, 95.00),
    ("Table",             "Furniture",       349.99, 140.00),
    ("Laptop",            "Technology",      899.99, 600.00),
    ("Monitor",           "Technology",      349.99, 210.00),
    ("Keyboard",          "Technology",      49.99,  22.00),
    ("USB Hub",           "Technology",      24.99,  9.50),
    ("Printer",           "Technology",      199.99, 110.00),
    ("Headphones",        "Technology",      79.99,  35.00),
    ("Notebooks",         "Office Supplies", 12.49,  4.50),
]

regions = ["East", "West", "Central", "South"]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]

start_date = date(2024, 1, 1)

rows = []
order_id = 1000
for _ in range(300):
    order_date = start_date + timedelta(days=random.randint(0, 364))
    product = random.choice(products)
    qty = random.randint(1, 10)
    unit_price = product[2]
    unit_cost = product[3]
    discount = random.choice([0.0, 0.0, 0.0, 0.05, 0.10, 0.15, 0.20])
    sale_price = round(unit_price * (1 - discount), 2)
    revenue = round(sale_price * qty, 2)
    profit = round((sale_price - unit_cost) * qty, 2)
    rows.append({
        "Order_ID": f"ORD-{order_id}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Ship_Mode": random.choice(ship_modes),
        "Region": random.choice(regions),
        "Category": product[1],
        "Product_Name": product[0],
        "Unit_Price": unit_price,
        "Discount": discount,
        "Sale_Price": sale_price,
        "Quantity": qty,
        "Revenue": revenue,
        "Cost": round(unit_cost * qty, 2),
        "Profit": profit,
    })
    order_id += 1

os.makedirs("data", exist_ok=True)
fieldnames = ["Order_ID","Order_Date","Ship_Mode","Region","Category",
              "Product_Name","Unit_Price","Discount","Sale_Price","Quantity",
              "Revenue","Cost","Profit"]

with open("data/superstore_orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Dataset created: {len(rows)} rows saved to data/superstore_orders.csv")
