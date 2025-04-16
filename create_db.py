import sqlite3
import pandas as pd


conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)


if ('sales',) not in tables:
    print("Table 'sales' not found! Creating it...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Product TEXT,
        Quantity INTEGER,
        Price REAL,
        Date TEXT
    )
    ''')
    print("Table 'sales' created.")
else:
    print("Table 'sales' exists.")


query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)


print(df)


conn.close()



