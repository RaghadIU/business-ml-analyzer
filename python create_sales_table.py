import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
''')

# Insert some sample sales data
sample_data = [
    ('2024-12-01', 'Product A', 10, 15.5),
    ('2024-12-02', 'Product B', 5, 25.0),
    ('2024-12-03', 'Product A', 7, 15.5),
    ('2024-12-04', 'Product C', 3, 40.0),
    ('2024-12-05', 'Product B', 2, 25.0),
    ('2024-12-06', 'Product A', 8, 15.5),
    ('2024-12-07', 'Product C', 1, 40.0)
]

cursor.executemany('''
    INSERT INTO sales (date, product, quantity, price)
    VALUES (?, ?, ?, ?)
''', sample_data)

# Save and close
conn.commit()
conn.close()

print("✅")
