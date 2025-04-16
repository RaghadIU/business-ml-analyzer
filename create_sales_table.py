import sqlite3


conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date TEXT,
    Product TEXT,
    Quantity INTEGER,
    Price REAL
)
""")


sample_data = [
    ("2024-01-01", "Product A", 10, 20.5),
    ("2024-01-02", "Product B", 5, 15.0),
    ("2024-01-03", "Product A", 8, 22.0),
]

cursor.executemany("INSERT INTO sales (Date, Product, Quantity, Price) VALUES (?, ?, ?, ?)", sample_data)


conn.commit()
conn.close()

print("✅ ")
