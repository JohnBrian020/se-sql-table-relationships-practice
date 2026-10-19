import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

q = """PRAGMA table_info(orders)"""

#q = """SELECT firstName, lastName, city, state FROM employees JOIN offices USING(officeCode) ORDER BY firstName, lastName;"""
#df = pd.read_sql(q, conn)
#print(df)

q = """SELECT contactfirstName, contactlastName ,orderNumber, orderDate, status FROM customers JOIN orders USING(customerNumber);"""
#df = pd.read_sql(q, conn)
#print(df.head())

q = """SELECT contactfirstName, contactlastName,checkNumber, paymentDate, amount FROM customers JOIN payments USING(customerNumber) ORDER BY amount DESC;"""
#df = pd.read_sql(q, conn)
#print(df.head())

q = """
SELECT
    contactFirstName,
    contactLastName,
    productName,
    quantityOrdered,
    orderDate
FROM customers
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
JOIN products
    USING (productCode)
ORDER BY orderDate DESC
;"""
df = pd.read_sql(q, conn)
print((df))
df.head()

conn.close()

