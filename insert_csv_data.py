'''import sqlite3
import pandas as pd

df = pd.read_csv("company_sales.csv") 
conn = sqlite3.connect("sales_data.db")
df.to_sql("sales", conn, if_exists="append", index=False)

conn.close()'''

