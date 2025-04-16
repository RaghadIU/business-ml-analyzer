import sqlite3
import pandas as pd

# إنشاء قاعدة البيانات أو الاتصال بها
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# التحقق من الجداول الموجودة في قاعدة البيانات
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# التحقق إذا كان جدول sales موجود
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

# تحميل البيانات من جدول sales
query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)

# عرض البيانات
print(df)

# إغلاق الاتصال
conn.close()



