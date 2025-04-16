import sqlite3


conn = sqlite3.connect('sales_data.db')  
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📋")
for table in tables:
    print(f"- {table[0]}")
