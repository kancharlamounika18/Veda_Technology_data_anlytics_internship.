from pathlib import Path
import re

ROOT = Path('/home/ubuntu/SQL-Filtering-Practice')
ROOT.mkdir(parents=True, exist_ok=True)
DUMP = Path('/home/ubuntu/work/northwind.sql')

def split_values(text):
    vals, cur, quoted = [], [], False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "'":
            cur.append(ch)
            if quoted and i + 1 < len(text) and text[i+1] == "'":
                cur.append("'"); i += 1
            else: quoted = not quoted
        elif ch == ',' and not quoted:
            vals.append(''.join(cur).strip()); cur=[]
        else: cur.append(ch)
        i += 1
    vals.append(''.join(cur).strip())
    return vals

def parse(v):
    if v.upper() == 'NULL': return None
    if len(v)>=2 and v[0]=="'" and v[-1]=="'": return v[1:-1].replace("''", "'")
    try: return float(v) if '.' in v else int(v)
    except: return v

def load(table):
    pat = re.compile(rf"INSERT INTO {table} VALUES \((.*)\);", re.I)
    return [[parse(v) for v in split_values(m.group(1))] for line in DUMP.read_text(encoding='utf-8').splitlines() if (m:=pat.match(line))]

customers = [dict(zip(['CustomerID','CompanyName','ContactName','ContactTitle','Address','City','Region','PostalCode','Country','Phone','Fax'], r)) for r in load('customers')]
products = [dict(zip(['ProductID','ProductName','SupplierID','CategoryID','QuantityPerUnit','UnitPrice','UnitsInStock','UnitsOnOrder','ReorderLevel','Discontinued'], r)) for r in load('products')]

def like(text, pattern):
    # Enough for the simple % patterns used here.
    p = pattern.replace('%','')
    if pattern.startswith('%') and pattern.endswith('%'): return p.lower() in text.lower()
    if pattern.startswith('%'): return text.lower().endswith(p.lower())
    if pattern.endswith('%'): return text.lower().startswith(p.lower())
    return text.lower() == p.lower()

def out(rows, cols, limit=12):
    shown = rows[:limit]
    lines = ['-- Expected result preview (first %d of %d row(s)):' % (len(shown), len(rows))]
    lines.append('-- ' + ' | '.join(cols))
    for r in shown:
        lines.append('-- ' + ' | '.join('NULL' if r.get(c) is None else (f"{r[c]:.2f}" if isinstance(r[c],float) else str(r[c])) for c in cols))
    if len(rows)>limit: lines.append(f'-- ... {len(rows)-limit} additional row(s)')
    return '\n'.join(lines)

Q=[]
def add(title, sql, rows, cols):
    Q.append((title, sql, out(rows, cols)))

add('USA customers', "SELECT CustomerID, CompanyName, Country\nFROM Customers\nWHERE Country = 'USA';", [r for r in customers if r['Country']=='USA'], ['CustomerID','CompanyName','Country'])
add('Customers in selected countries', "SELECT CustomerID, CompanyName, Country\nFROM Customers\nWHERE Country IN ('USA', 'UK', 'Germany');", [r for r in customers if r['Country'] in {'USA','UK','Germany'}], ['CustomerID','CompanyName','Country'])
add('Products in a price range', "SELECT ProductID, ProductName, UnitPrice\nFROM Products\nWHERE UnitPrice BETWEEN 20 AND 50\nORDER BY UnitPrice ASC;", sorted([r for r in products if 20 <= r['UnitPrice'] <= 50], key=lambda x:x['UnitPrice']), ['ProductID','ProductName','UnitPrice'])
add('Products outside a price range', "SELECT ProductID, ProductName, UnitPrice\nFROM Products\nWHERE UnitPrice NOT BETWEEN 10 AND 20\nORDER BY UnitPrice ASC;", sorted([r for r in products if not (10 <= r['UnitPrice'] <= 20)], key=lambda x:x['UnitPrice']), ['ProductID','ProductName','UnitPrice'])
add("Products beginning with Ch", "SELECT ProductID, ProductName, UnitPrice\nFROM Products\nWHERE ProductName LIKE 'Ch%';", [r for r in products if like(r['ProductName'],'Ch%')], ['ProductID','ProductName','UnitPrice'])
add('Companies containing Market', "SELECT CustomerID, CompanyName, City\nFROM Customers\nWHERE CompanyName LIKE '%Market%';", [r for r in customers if like(r['CompanyName'],'%Market%')], ['CustomerID','CompanyName','City'])
add('Customers in Brazil, France, or UK', "SELECT CustomerID, CompanyName, Country\nFROM Customers\nWHERE Country IN ('Brazil', 'France', 'UK')\nORDER BY Country, CompanyName;", sorted([r for r in customers if r['Country'] in {'Brazil','France','UK'}], key=lambda x:(x['Country'],x['CompanyName'])), ['CustomerID','CompanyName','Country'])
add('Cities beginning with L', "SELECT CustomerID, CompanyName, City, Country\nFROM Customers\nWHERE City LIKE 'L%';", [r for r in customers if like(r['City'],'L%')], ['CustomerID','CompanyName','City','Country'])
add('High-priced active products', "SELECT ProductID, ProductName, UnitPrice, Discontinued\nFROM Products\nWHERE UnitPrice > 50 AND Discontinued = 0\nORDER BY UnitPrice DESC;", sorted([r for r in products if r['UnitPrice']>50 and r['Discontinued']==0], key=lambda x:x['UnitPrice'], reverse=True), ['ProductID','ProductName','UnitPrice','Discontinued'])
add('Contact names ending with er', "SELECT CustomerID, CompanyName, ContactName\nFROM Customers\nWHERE ContactName LIKE '%er';", [r for r in customers if r['ContactName'] and like(r['ContactName'],'%er')], ['CustomerID','CompanyName','ContactName'])
add('Tea products in a price range', "SELECT ProductID, ProductName, UnitPrice\nFROM Products\nWHERE UnitPrice BETWEEN 10 AND 30\nAND ProductName LIKE '%Tea%';", sorted([r for r in products if 10 <= r['UnitPrice'] <= 30 and like(r['ProductName'],'%Tea%')], key=lambda x:x['UnitPrice']), ['ProductID','ProductName','UnitPrice'])
add('Specific cities using IN', "SELECT CustomerID, CompanyName, City, Country\nFROM Customers\nWHERE City IN ('London', 'Berlin', 'Paris')\nORDER BY City, CompanyName;", sorted([r for r in customers if r['City'] in {'London','Berlin','Paris'}], key=lambda x:(x['City'],x['CompanyName'])), ['CustomerID','CompanyName','City','Country'])

header = '''-- SQL FILTERING PRACTICE | DAY 22 OF 45
-- Veda Technology – Data Analytics Internship
-- GitHub repository name: SQL-Filtering-Practice
-- Dataset: Northwind
-- Topics: WHERE, IN, BETWEEN, NOT BETWEEN, LIKE, AND, ORDER BY
--
-- Run each query separately in MySQL or PostgreSQL.
-- The result previews below are embedded in this single file as comments.

'''
sections=[]
for i,(title,sql,result) in enumerate(Q,1):
    sections.append(f"-- ============================================================================\n-- QUERY {i}: {title}\n-- ============================================================================\n{sql}\n\n{result}\n")
footer='''\n-- ============================================================================
-- INTERVIEW NOTES
-- ============================================================================
-- LIKE is used for pattern matching, for example ProductName LIKE 'Ch%'.
-- The % wildcard represents zero or more characters.
-- Use = when you need an exact match, such as Country = 'USA'.
-- BETWEEN is useful for inclusive ranges, such as UnitPrice BETWEEN 20 AND 50.
-- IN is useful when matching one column against several exact values.
'''
(ROOT/'sql_filtering_practice.sql').write_text(header+'\n'.join(sections)+footer, encoding='utf-8')
print(ROOT/'sql_filtering_practice.sql')
print('queries:',len(Q),'customers:',len(customers),'products:',len(products))
for i,(_,_,_) in enumerate(Q,1): print('query',i,'ready')
