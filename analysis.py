# analysis.py
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("First 5 rows:")
    print(df.head())
    print("\nSummary:")
    print(df.describe())
    return df

if __name__ == "__main__":
    data_path = "data/sales.csv"  
    load_data(data_path)
