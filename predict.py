# predict.py
import pandas as pd
import pickle
import datetime

def load_model(path="models/sales_model.pkl"):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model

def get_latest_day(csv_path="data/sales.csv"):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    last_date = df['Date'].max()
    return last_date

def predict_future_sales(days_ahead):
    model = load_model()
    last_date = get_latest_day()
    
    future_day = (last_date + datetime.timedelta(days=days_ahead))
    day_number = (future_day - df['Date'].min()).days

    prediction = model.predict([[day_number]])
    
    print(f"📅 Date: {future_day.date()}")
    print(f"📈 Predicted Sales: ${prediction[0]:.2f}")

if __name__ == "__main__":
    days = int(input("🔮 Enter number of days in the future to predict: "))
    
    
    df = pd.read_csv("data/sales.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    
    predict_future_sales(days)
