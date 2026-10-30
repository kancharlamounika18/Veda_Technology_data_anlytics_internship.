import pandas as pd
import numpy as np
import os

def generate_retail_dataset():
    np.random.seed(42)
    n_rows = 500

    order_ids = [f"CA-2024-{100000 + i}" for i in range(n_rows)]
    
    start_date = pd.to_datetime("2024-01-01")
    end_date = pd.to_datetime("2024-12-31")
    random_days = np.random.randint(0, (end_date - start_date).days, n_rows)
    order_dates = [start_date + pd.Timedelta(days=int(d)) for d in random_days]
    ship_days = np.random.choice([1, 2, 3, 5, 7], size=n_rows, p=[0.1, 0.2, 0.35, 0.25, 0.1])
    ship_dates = [od + pd.Timedelta(days=int(sd)) for od, sd in zip(order_dates, ship_days)]
    
    ship_modes = []
    for sd in ship_days:
        if sd == 1:
            ship_modes.append("Same Day")
        elif sd == 2:
            ship_modes.append("First Class")
        elif sd <= 4:
            ship_modes.append("Second Class")
        else:
            ship_modes.append("Standard Class")

    segments = np.random.choice(["Consumer", "Corporate", "Home Office"], size=n_rows, p=[0.52, 0.30, 0.18])
    regions = np.random.choice(["East", "West", "Central", "South"], size=n_rows, p=[0.30, 0.32, 0.22, 0.16])
    
    region_cities = {
        "East": [("New York", "New York"), ("Philadelphia", "Pennsylvania"), ("Boston", "Massachusetts")],
        "West": [("Los Angeles", "California"), ("Seattle", "Washington"), ("San Francisco", "California")],
        "Central": [("Chicago", "Illinois"), ("Houston", "Texas"), ("Detroit", "Michigan")],
        "South": [("Atlanta", "Georgia"), ("Miami", "Florida"), ("Charlotte", "North Carolina")]
    }
    
    cities = []
    states = []
    for r in regions:
        choice = region_cities[r][np.random.choice(len(region_cities[r]))]
        cities.append(choice[0])
        states.append(choice[1])

    catalog = {
        "Technology": [
            ("Phones", "Apple iPhone 15 Pro", 999.00, 0.25),
            ("Phones", "Samsung Galaxy S24", 849.00, 0.22),
            ("Accessories", "Logitech MX Master 3S Mouse", 99.00, 0.35),
            ("Machines", "HP LaserJet Pro Multifunction Printer", 450.00, 0.18),
            ("Copiers", "Canon ImageCLASS Copier", 1199.00, 0.30)
        ],
        "Furniture": [
            ("Chairs", "Herman Miller Ergonomic Task Chair", 650.00, 0.20),
            ("Tables", "BPI Conference Room Table", 890.00, 0.15),
            ("Bookcases", "Bush Mission Oak 4-Shelf Bookcase", 320.00, 0.12),
            ("Furnishings", "Deflecto Executive Desk Pad", 45.00, 0.40)
        ],
        "Office Supplies": [
            ("Binders", "GBC Heavy-Duty Binder 3-Inch", 28.00, 0.45),
            ("Paper", "Hammermill Premium Multipurpose Paper 500ct", 14.50, 0.38),
            ("Storage", "Fellowes Heavy-Duty Storage Boxes 12pk", 75.00, 0.25),
            ("Appliances", "Krups 12-Cup Programmable Coffee Maker", 85.00, 0.28),
            ("Envelopes", "Quality Park Security Envelopes 500ct", 22.00, 0.42),
            ("Art", "Prismacolor Premier Colored Pencils 72ct", 52.00, 0.35)
        ]
    }

    categories = np.random.choice(["Technology", "Furniture", "Office Supplies"], size=n_rows, p=[0.28, 0.32, 0.40])
    
    sub_cats = []
    products = []
    sales = []
    quantities = []
    discounts = []
    profits = []

    for cat in categories:
        items = catalog[cat]
        item = items[np.random.choice(len(items))]
        sub_cat, prod_name, base_price, base_margin = item
        
        qty = np.random.randint(1, 11)
        discount = float(np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40], p=[0.40, 0.15, 0.15, 0.12, 0.08, 0.06, 0.04]))
        
        sale_price = base_price * (1.0 - discount)
        total_sale = round(sale_price * qty, 2)
        
        cost_per_unit = base_price * (1.0 - base_margin)
        total_cost = cost_per_unit * qty
        profit = round(total_sale - total_cost, 2)
        
        sub_cats.append(sub_cat)
        products.append(prod_name)
        quantities.append(qty)
        discounts.append(discount)
        sales.append(total_sale)
        profits.append(profit)

    df = pd.DataFrame({
        "Order_ID": order_ids,
        "Order_Date": [d.strftime("%Y-%m-%d") for d in order_dates],
        "Ship_Date": [d.strftime("%Y-%m-%d") for d in ship_dates],
        "Ship_Mode": ship_modes,
        "Customer_Segment": segments,
        "Country": ["United States"] * n_rows,
        "City": cities,
        "State": states,
        "Region": regions,
        "Category": categories,
        "Sub_Category": sub_cats,
        "Product_Name": products,
        "Sales": sales,
        "Quantity": quantities,
        "Discount": discounts,
        "Profit": profits
    })

    # Sort raw data by Order_Date as standard historical log
    df = df.sort_values(by="Order_Date").reset_index(drop=True)

    out_csv = "data/superstore_retail_sales.csv"
    df.to_csv(out_csv, index=False)
    print(f"Generated {len(df)} rows saved to {out_csv}")
    return df

if __name__ == "__main__":
    generate_retail_dataset()
