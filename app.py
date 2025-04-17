import streamlit as st
import pandas as pd
import pickle
import datetime
import sqlite3
import matplotlib.pyplot as plt

# Load the model (use st.cache_resource for models)
@st.cache_resource
def load_model():
    with open("models/sales_model.pkl", "rb") as f:
        return pickle.load(f)

# Load the data from SQLite database
@st.cache_data
def load_data():
    conn = sqlite3.connect('sales_data.db')
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Ensure proper date conversion
    df = df.dropna(subset=['Date'])  # Remove rows where Date conversion failed
    conn.close()
    return df

# Predict sales based on the selected date
def predict_sales(target_date, model, df):
    target_date = pd.Timestamp(target_date)
    day_number = (target_date - df['Date'].min()).days
    prediction = model.predict([[day_number]])[0]
    return target_date.date(), prediction

# Plot sales data for all products
def plot_sales_all_products(df, target_date, predicted_sales):
    fig, ax = plt.subplots(figsize=(10,6))
    
    # Loop through each product and plot its sales
    products = df['Product'].unique()
    for product in products:
        product_data = df[df['Product'] == product]
        ax.plot(product_data['Date'], product_data['Sales'], label=f'Sales for {product}')
    
    # Plot the predicted sales point for each product
    ax.scatter(target_date, predicted_sales, color='red', label='Predicted Sales', zorder=5)
    
    ax.set_title("Sales Over Time with Prediction for All Products")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

# Plot sales for a specific product
def plot_sales_per_product(df, product, target_date, predicted_sales):
    fig, ax = plt.subplots(figsize=(10,6))
    
    product_data = df[df['Product'] == product]
    ax.plot(product_data['Date'], product_data['Sales'], label=f'Sales for {product}')
    
    # Plot the predicted sales point for the product
    ax.scatter(target_date, predicted_sales, color='red', label=f'Predicted Sales for {product}', zorder=5)
    
    ax.set_title(f"Sales Over Time with Prediction for {product}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

# ---------------- Streamlit interface ----------------
st.title("🔍 Business Sales Predictor")
st.write("Predict future sales using AI 🧠📈")

# Load data before using it
df = load_data()

# Show available columns in the dataset


# Add a 'Sales' column if not already present
if 'Sales' not in df.columns:
    df['Sales'] = df['Quantity'] * df['Price']

# === Dashboard Statistics ===
total_sales = df['Sales'].sum()
total_quantity = df['Quantity'].sum()
max_sales_date = df.loc[df['Sales'].idxmax()]['Date']
min_sales_date = df.loc[df['Sales'].idxmin()]['Date']

st.subheader("Quick Business Stats")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📦 Total Quantity Sold", int(total_quantity))
col3.metric("📅 Best Sales Day", str(max_sales_date.date()))
col4.metric("📅 Lowest Sales Day", str(min_sales_date.date()))

# Date input using the calendar widget
target_date = st.date_input("Select the target date:", min_value=df['Date'].max() + datetime.timedelta(days=1))

if st.button("Predict Sales"):
    model = load_model()
    future_date, predicted_sales = predict_sales(target_date, model, df)
    
    st.success(f"📅 Predicted Date: {future_date}")
    st.info(f"💰 Predicted Sales: ${predicted_sales:.2f}")
    
    # Plot the sales data for all products
    plot_sales_all_products(df, future_date, predicted_sales)

    # Option to plot for a specific product
    product = st.selectbox("Select a product to see its individual sales", df['Product'].unique())
    plot_sales_per_product(df, product, future_date, predicted_sales)
