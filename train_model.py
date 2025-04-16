# train_model.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pickle
import os

def prepare_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total'] = df['Quantity'] * df['Price']

    # تحويل التاريخ إلى رقم (أيام منذ أول تاريخ)
    df = df.sort_values("Date")
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days

    return df[['Days', 'Total']]

def train_and_save_model(df):
    X = df[['Days']]
    y = df['Total']

    model = LinearRegression()
    model.fit(X, y)

    # حفظ النموذج في ملف
    os.makedirs("models", exist_ok=True)
    with open("models/sales_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved successfully!")

    # رسم البيانات والنموذج
    plt.scatter(X, y, label="Actual Sales")
    plt.plot(X, model.predict(X), color='red', label="Predicted Sales")
    plt.xlabel("Days since start")
    plt.ylabel("Total Sales")
    plt.title("Sales Prediction Model")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = prepare_data("data/sales.csv")
    train_and_save_model(df)
