from pathlib import Path
import re

ROOT=Path('/home/ubuntu/SQL-Aggregation-Basics')
ROOT.mkdir(parents=True,exist_ok=True)
DUMP=Path('/home/ubuntu/work/northwind.sql')

def split_values(text):
    vals=[]; cur=[]; quoted=False; i=0
    while i<len(text):
        ch=text[i]
        if ch=="'":
            cur.append(ch)
            if quoted and i+1<len(text) and text[i+1]=="'": cur.append("'"); i+=1
            else: quoted=not quoted
        elif ch==',' and not quoted: vals.append(''.join(cur).strip()); cur=[]
        else: cur.append(ch)
        i+=1
    vals.append(''.join(cur).strip()); return vals

def parse(v):
    if v.upper()=='NULL': return None
    if len(v)>=2 and v[0]=="'" and v[-1]=="'": return v[1:-1].replace("''", "'")
    try: return float(v) if '.' in v else int(v)
    except: return v

def load(table):
    pat=re.compile(rf"INSERT INTO {table} VALUES \((.*)\);",re.I)
    return [[parse(v) for v in split_values(m.group(1))] for line in DUMP.read_text(encoding='utf-8').splitlines() if (m:=pat.match(line))]

customers=[dict(zip(['CustomerID','CompanyName','ContactName','ContactTitle','Address','City','Region','PostalCode','Country','Phone','Fax'],r)) for r in load('customers')]
products=[dict(zip(['ProductID','ProductName','SupplierID','CategoryID','QuantityPerUnit','UnitPrice','UnitsInStock','UnitsOnOrder','ReorderLevel','Discontinued'],r)) for r in load('products')]
categories=[dict(zip(['CategoryID','CategoryName','Description','Picture'],r)) for r in load('categories')]
cat={r['CategoryID']:r['CategoryName'] for r in categories}

def val(x):
    if x is None:return 'NULL'
    if isinstance(x,float):return f'{x:.2f}'
    return str(x)

def result(cols, rows, limit=12):
    show=rows[:limit]
    s=['-- Expected result preview (%d of %d row(s)):'%(len(show),len(rows)),'-- '+' | '.join(cols)]
    s += ['-- '+' | '.join(val(r.get(c)) for c in cols) for r in show]
    if len(rows)>limit:s.append(f'-- ... {len(rows)-limit} additional row(s)')
    return '\n'.join(s)

queries=[]
def add(title,sql,cols,rows):queries.append((title,sql,result(cols,rows)))
add('Total number of customers','SELECT COUNT(*) AS TotalCustomers\nFROM Customers;',['TotalCustomers'],[{'TotalCustomers':len(customers)}])
add('Total number of products','SELECT COUNT(*) AS TotalProducts\nFROM Products;',['TotalProducts'],[{'TotalProducts':len(products)}])
add('Total units in stock','SELECT SUM(UnitsInStock) AS TotalUnitsInStock\nFROM Products;',['TotalUnitsInStock'],[{'TotalUnitsInStock':sum(r['UnitsInStock'] or 0 for r in products)}])
add('Average product price','SELECT AVG(UnitPrice) AS AverageUnitPrice\nFROM Products;',['AverageUnitPrice'],[{'AverageUnitPrice':sum(r['UnitPrice'] for r in products)/len(products)}])
add('Minimum and maximum product price','SELECT MIN(UnitPrice) AS MinimumPrice, MAX(UnitPrice) AS MaximumPrice\nFROM Products;',['MinimumPrice','MaximumPrice'],[{'MinimumPrice':min(r['UnitPrice'] for r in products),'MaximumPrice':max(r['UnitPrice'] for r in products)}])
by_country=[]
for country in sorted({r['Country'] for r in customers}): by_country.append({'Country':country,'CustomerCount':sum(r['Country']==country for r in customers)})
add('Customers by country','SELECT Country, COUNT(*) AS CustomerCount\nFROM Customers\nGROUP BY Country\nORDER BY CustomerCount DESC;',['Country','CustomerCount'],sorted(by_country,key=lambda r:(-r['CustomerCount'],r['Country'])))
by_cat=[]
for cid,name in cat.items():
    ps=[r for r in products if r['CategoryID']==cid]
    by_cat.append({'CategoryName':name,'ProductCount':len(ps),'AveragePrice':sum(r['UnitPrice'] for r in ps)/len(ps)})
add('Product count and average price by category','SELECT c.CategoryName, COUNT(p.ProductID) AS ProductCount, AVG(p.UnitPrice) AS AveragePrice\nFROM Categories c\nJOIN Products p ON c.CategoryID = p.CategoryID\nGROUP BY c.CategoryName\nORDER BY AveragePrice DESC;',['CategoryName','ProductCount','AveragePrice'],sorted(by_cat,key=lambda r:(-r['AveragePrice'],r['CategoryName'])))
by_disc=[]
for d in [0,1]:
 ps=[r for r in products if r['Discontinued']==d]
 by_disc.append({'Discontinued':d,'ProductCount':len(ps),'AveragePrice':sum(r['UnitPrice'] for r in ps)/len(ps)})
add('Products by discontinued status','SELECT Discontinued, COUNT(*) AS ProductCount, AVG(UnitPrice) AS AveragePrice\nFROM Products\nGROUP BY Discontinued;',['Discontinued','ProductCount','AveragePrice'],by_disc)
by_supplier=[]
for sid in sorted({r['SupplierID'] for r in products}):
 ps=[r for r in products if r['SupplierID']==sid]
 by_supplier.append({'SupplierID':sid,'ProductCount':len(ps),'MinimumPrice':min(r['UnitPrice'] for r in ps),'MaximumPrice':max(r['UnitPrice'] for r in ps)})
add('Price range by supplier','SELECT SupplierID, COUNT(*) AS ProductCount, MIN(UnitPrice) AS MinimumPrice, MAX(UnitPrice) AS MaximumPrice\nFROM Products\nGROUP BY SupplierID\nORDER BY SupplierID;',['SupplierID','ProductCount','MinimumPrice','MaximumPrice'],by_supplier)
inv=[]
for cid,name in cat.items():
 ps=[r for r in products if r['CategoryID']==cid]
 inv.append({'CategoryName':name,'InventoryValue':sum((r['UnitPrice'] or 0)*(r['UnitsInStock'] or 0) for r in ps)})
add('Inventory value by category','SELECT c.CategoryName, SUM(p.UnitPrice * p.UnitsInStock) AS InventoryValue\nFROM Categories c\nJOIN Products p ON c.CategoryID = p.CategoryID\nGROUP BY c.CategoryName\nORDER BY InventoryValue DESC;',['CategoryName','InventoryValue'],sorted(inv,key=lambda r:(-r['InventoryValue'],r['CategoryName'])))

header='''-- SQL AGGREGATION BASICS | DAY 23 OF 45\n-- Veda Technology – Data Analytics Internship\n-- GitHub repository name: SQL-Aggregation-Basics\n-- Dataset: Northwind\n-- Topics: COUNT, SUM, AVG, MIN, MAX, GROUP BY, JOIN\n--\n-- Run each query separately in MySQL or PostgreSQL.\n-- Expected result previews are included below as SQL comments.\n\n'''
parts=[]
for i,(title,sql,res) in enumerate(queries,1):
 parts.append(f'-- ============================================================================\n-- QUERY {i}: {title}\n-- ============================================================================\n{sql}\n\n{res}\n')
footer='''-- ============================================================================\n-- INTERVIEW NOTES\n-- ============================================================================\n-- GROUP BY combines rows with the same value so aggregate functions can be\n-- calculated for each group, such as customers per country.\n-- AVG ignores NULL values. COUNT(*) counts rows, while COUNT(column) ignores\n-- NULL values in that column.\n-- SUM, MIN, and MAX also ignore NULL values.\n'''
(ROOT/'sql_aggregation_basics.sql').write_text(header+'\n'.join(parts)+footer,encoding='utf-8')
print(ROOT/'sql_aggregation_basics.sql')
print('queries',len(queries))
