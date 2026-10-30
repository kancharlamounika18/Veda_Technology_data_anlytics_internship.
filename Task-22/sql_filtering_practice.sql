-- SQL FILTERING PRACTICE | DAY 22 OF 45
-- Veda Technology – Data Analytics Internship
-- GitHub repository name: SQL-Filtering-Practice
-- Dataset: Northwind
-- Topics: WHERE, IN, BETWEEN, NOT BETWEEN, LIKE, AND, ORDER BY
--
-- Run each query separately in MySQL or PostgreSQL.
-- The result previews below are embedded in this single file as comments.

-- ============================================================================
-- QUERY 1: USA customers
-- ============================================================================
SELECT CustomerID, CompanyName, Country
FROM Customers
WHERE Country = 'USA';

-- Expected result preview (first 12 of 13 row(s)):
-- CustomerID | CompanyName | Country
-- GREAL | Great Lakes Food Market | USA
-- HUNGC | Hungry Coyote Import Store | USA
-- LAZYK | Lazy K Kountry Store | USA
-- LETSS | Let's Stop N Shop | USA
-- LONEP | Lonesome Pine Restaurant | USA
-- OLDWO | Old World Delicatessen | USA
-- RATTC | Rattlesnake Canyon Grocery | USA
-- SAVEA | Save-a-lot Markets | USA
-- SPLIR | Split Rail Beer & Ale | USA
-- THEBI | The Big Cheese | USA
-- THECR | The Cracker Box | USA
-- TRAIH | Trail's Head Gourmet Provisioners | USA
-- ... 1 additional row(s)

-- ============================================================================
-- QUERY 2: Customers in selected countries
-- ============================================================================
SELECT CustomerID, CompanyName, Country
FROM Customers
WHERE Country IN ('USA', 'UK', 'Germany');

-- Expected result preview (first 12 of 31 row(s)):
-- CustomerID | CompanyName | Country
-- ALFKI | Alfreds Futterkiste | Germany
-- AROUT | Around the Horn | UK
-- BLAUS | Blauer See Delikatessen | Germany
-- BSBEV | B's Beverages | UK
-- CONSH | Consolidated Holdings | UK
-- DRACD | Drachenblut Delikatessen | Germany
-- EASTC | Eastern Connection | UK
-- FRANK | Frankenversand | Germany
-- GREAL | Great Lakes Food Market | USA
-- HUNGC | Hungry Coyote Import Store | USA
-- ISLAT | Island Trading | UK
-- KOENE | Königlich Essen | Germany
-- ... 19 additional row(s)

-- ============================================================================
-- QUERY 3: Products in a price range
-- ============================================================================
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 20 AND 50
ORDER BY UnitPrice ASC;

-- Expected result preview (first 12 of 31 row(s)):
-- ProductID | ProductName | UnitPrice
-- 49 | Maxilaku | 20
-- 11 | Queso Cabrales | 21
-- 22 | Gustaf's Knäckebröd | 21
-- 65 | Louisiana Fiery Hot Pepper Sauce | 21.05
-- 5 | Chef Anton's Gumbo Mix | 21.35
-- 71 | Flotemysost | 21.50
-- 4 | Chef Anton's Cajun Seasoning | 22
-- 14 | Tofu | 23.25
-- 55 | Pâté chinois | 24
-- 6 | Grandma's Boysenberry Spread | 25
-- 30 | Nord-Ost Matjeshering | 25.89
-- 37 | Gravad lax | 26
-- ... 19 additional row(s)

-- ============================================================================
-- QUERY 4: Products outside a price range
-- ============================================================================
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice NOT BETWEEN 10 AND 20
ORDER BY UnitPrice ASC;

-- Expected result preview (first 12 of 48 row(s)):
-- ProductID | ProductName | UnitPrice
-- 33 | Geitost | 2.50
-- 24 | Guaraná Fantástica | 4.50
-- 13 | Konbu | 6
-- 52 | Filo Mix | 7
-- 54 | Tourtière | 7.45
-- 75 | Rhönbräu Klosterbier | 7.75
-- 23 | Tunnbröd | 9
-- 19 | Teatime Chocolate Biscuits | 9.20
-- 45 | Rogede sild | 9.50
-- 47 | Zaanse koeken | 9.50
-- 41 | Jack's New England Clam Chowder | 9.65
-- 11 | Queso Cabrales | 21
-- ... 36 additional row(s)

-- ============================================================================
-- QUERY 5: Products beginning with Ch
-- ============================================================================
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE ProductName LIKE 'Ch%';

-- Expected result preview (first 6 of 6 row(s)):
-- ProductID | ProductName | UnitPrice
-- 1 | Chai | 18
-- 2 | Chang | 19
-- 4 | Chef Anton's Cajun Seasoning | 22
-- 5 | Chef Anton's Gumbo Mix | 21.35
-- 39 | Chartreuse verte | 18
-- 48 | Chocolade | 12.75

-- ============================================================================
-- QUERY 6: Companies containing Market
-- ============================================================================
SELECT CustomerID, CompanyName, City
FROM Customers
WHERE CompanyName LIKE '%Market%';

-- Expected result preview (first 4 of 4 row(s)):
-- CustomerID | CompanyName | City
-- BOTTM | Bottom-Dollar Markets | Tsawassen
-- GREAL | Great Lakes Food Market | Eugene
-- SAVEA | Save-a-lot Markets | Boise
-- WHITC | White Clover Markets | Seattle

-- ============================================================================
-- QUERY 7: Customers in Brazil, France, or UK
-- ============================================================================
SELECT CustomerID, CompanyName, Country
FROM Customers
WHERE Country IN ('Brazil', 'France', 'UK')
ORDER BY Country, CompanyName;

-- Expected result preview (first 12 of 27 row(s)):
-- CustomerID | CompanyName | Country
-- COMMI | Comércio Mineiro | Brazil
-- FAMIA | Familia Arquibaldo | Brazil
-- GOURL | Gourmet Lanchonetes | Brazil
-- HANAR | Hanari Carnes | Brazil
-- QUEDE | Que Delícia | Brazil
-- QUEEN | Queen Cozinha | Brazil
-- RICAR | Ricardo Adocicados | Brazil
-- TRADH | Tradição Hipermercados | Brazil
-- WELLI | Wellington Importadora | Brazil
-- BLONP | Blondesddsl père et fils | France
-- BONAP | Bon app' | France
-- DUMON | Du monde entier | France
-- ... 15 additional row(s)

-- ============================================================================
-- QUERY 8: Cities beginning with L
-- ============================================================================
SELECT CustomerID, CompanyName, City, Country
FROM Customers
WHERE City LIKE 'L%';

-- Expected result preview (first 12 of 13 row(s)):
-- CustomerID | CompanyName | City | Country
-- AROUT | Around the Horn | London | UK
-- BERGS | Berglunds snabbköp | Luleå | Sweden
-- BSBEV | B's Beverages | London | UK
-- CONSH | Consolidated Holdings | London | UK
-- EASTC | Eastern Connection | London | UK
-- FOLIG | Folies gourmandes | Lille | France
-- FURIB | Furia Bacalhau e Frutos do Mar | Lisboa | Portugal
-- MORGK | Morgenstern Gesundkost | Leipzig | Germany
-- NORTS | North/South | London | UK
-- PRINI | Princesa Isabel Vinhos | Lisboa | Portugal
-- SEVES | Seven Seas Imports | London | UK
-- SPLIR | Split Rail Beer & Ale | Lander | USA
-- ... 1 additional row(s)

-- ============================================================================
-- QUERY 9: High-priced active products
-- ============================================================================
SELECT ProductID, ProductName, UnitPrice, Discontinued
FROM Products
WHERE UnitPrice > 50 AND Discontinued = 0
ORDER BY UnitPrice DESC;

-- Expected result preview (first 5 of 5 row(s)):
-- ProductID | ProductName | UnitPrice | Discontinued
-- 38 | Côte de Blaye | 263.50 | 0
-- 20 | Sir Rodney's Marmalade | 81 | 0
-- 18 | Carnarvon Tigers | 62.50 | 0
-- 59 | Raclette Courdavault | 55 | 0
-- 51 | Manjimup Dried Apples | 53 | 0

-- ============================================================================
-- QUERY 10: Contact names ending with er
-- ============================================================================
SELECT CustomerID, CompanyName, ContactName
FROM Customers
WHERE ContactName LIKE '%er';

-- Expected result preview (first 10 of 10 row(s)):
-- CustomerID | CompanyName | ContactName
-- BOLID | Bólido Comidas preparadas | Martín Sommer
-- GREAL | Great Lakes Food Market | Howard Snyder
-- HUNGC | Hungry Coyote Import Store | Yoshi Latimer
-- KOENE | Königlich Essen | Philip Cramer
-- LEHMS | Lehmanns Marktstand | Renate Messner
-- MORGK | Morgenstern Gesundkost | Alexander Feuer
-- NORTS | North/South | Simon Crowther
-- SPECD | Spécialités du monde | Dominique Perrier
-- SPLIR | Split Rail Beer & Ale | Art Braunschweiger
-- WANDK | Die Wandernde Kuh | Rita Müller

-- ============================================================================
-- QUERY 11: Tea products in a price range
-- ============================================================================
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 30
AND ProductName LIKE '%Tea%';

-- Expected result preview (first 0 of 0 row(s)):
-- ProductID | ProductName | UnitPrice

-- ============================================================================
-- QUERY 12: Specific cities using IN
-- ============================================================================
SELECT CustomerID, CompanyName, City, Country
FROM Customers
WHERE City IN ('London', 'Berlin', 'Paris')
ORDER BY City, CompanyName;

-- Expected result preview (first 9 of 9 row(s)):
-- CustomerID | CompanyName | City | Country
-- ALFKI | Alfreds Futterkiste | Berlin | Germany
-- AROUT | Around the Horn | London | UK
-- BSBEV | B's Beverages | London | UK
-- CONSH | Consolidated Holdings | London | UK
-- EASTC | Eastern Connection | London | UK
-- NORTS | North/South | London | UK
-- SEVES | Seven Seas Imports | London | UK
-- PARIS | Paris spécialités | Paris | France
-- SPECD | Spécialités du monde | Paris | France

-- ============================================================================
-- INTERVIEW NOTES
-- ============================================================================
-- LIKE is used for pattern matching, for example ProductName LIKE 'Ch%'.
-- The % wildcard represents zero or more characters.
-- Use = when you need an exact match, such as Country = 'USA'.
-- BETWEEN is useful for inclusive ranges, such as UnitPrice BETWEEN 20 AND 50.
-- IN is useful when matching one column against several exact values.
