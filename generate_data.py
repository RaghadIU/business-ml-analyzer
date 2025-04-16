# generate_data.py
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# بيانات تجريبية
products = ['T-Shirt', 'Shoes', 'Jeans', 'Hat', 'Socks']
start_date = datetime(2024, 1, 1)
rows = []

for _ in range(100):  # عدد الصفوف
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = round(random.uniform(10, 100), 2)
    date = start_date + timedelta(days=random.randint(0, 90))
    rows.append([product, quantity, price, date.strftime("%Y-%m-%d")])

# إنشاء DataFrame
df = pd.DataFrame(rows, columns=["Product", "Quantity", "Price", "Date"])

# حفظه داخل مجلد data
os.makedirs("data", exist_ok=True)
df.to_csv("data/sales.csv", index=False)

print("✅ sales.csv file created successfully in data/")
