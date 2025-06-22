# scripts/forecast_spend.py

import pandas as pd
from prophet import Prophet
from pathlib import Path

# === Step 1: Load cleaned data ===
df = pd.read_csv("data/processed/clean_procurement_data.csv", parse_dates=["PO_Date"])

# === Step 2: Aggregate monthly spend ===
monthly_spend = (
    df.groupby(pd.Grouper(key="PO_Date", freq="M"))["total_spend"]
    .sum()
    .reset_index()
    .rename(columns={"PO_Date": "ds", "total_spend": "y"})
)

# === Step 3: Train Prophet Model ===
model = Prophet()
model.fit(monthly_spend)

# === Step 4: Create future dataframe & forecast ===
future = model.make_future_dataframe(periods=6, freq='M')
forecast = model.predict(future)

# === Step 5: Save forecast output ===
forecast_output = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
forecast_output.to_csv("data/processed/forecast_output.csv", index=False)

print("✅ Forecast saved to data/processed/forecast_output.csv")
print(forecast_output.tail(6))
