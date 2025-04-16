import sqlite3

# اتصل بقاعدة البيانات
conn = sqlite3.connect('sales_data.db')  # تأكد أن الملف فعلاً موجود بنفس المجلد
cursor = conn.cursor()

# استعرض كل الجداول الموجودة
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📋 الجداول الموجودة داخل قاعدة البيانات:")
for table in tables:
    print(f"- {table[0]}")
