# generate_data.py
import pandas as pd
from datetime import datetime, timedelta
import random
import os


products = ['T-Shirt', 'Shoes', 'Jeans', 'Hat', 'Socks']
start_date = datetime(2024, 1, 1)
rows = []

for _ in range(100): 
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = round(random.uniform(10, 100), 2)
    date = start_date + timedelta(days=random.randint(0, 90))
    rows.append([product, quantity, price, date.strftime("%Y-%m-%d")])


df = pd.DataFrame(rows, columns=["Product", "Quantity", "Price", "Date"])


os.makedirs("data", exist_ok=True)
df.to_csv("data/sales.csv", index=False)

print("sales.csv file created successfully in data/")
