'''import sqlite3
import pandas as pd

# تحميل البيانات من ملف CSV
df = pd.read_csv("company_sales.csv")  # تأكد من اسم الملف

# الاتصال بقاعدة البيانات
conn = sqlite3.connect("sales_data.db")
df.to_sql("sales", conn, if_exists="append", index=False)

conn.close()
print("✅ تم إضافة بيانات الشركة إلى قاعدة البيانات.")'''
