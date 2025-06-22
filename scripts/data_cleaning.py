# scripts/data_cleaning.py

import pandas as pd
from pathlib import Path

# === Step 1: Load the raw procurement data ===
raw_path = Path("data/raw/sample_procurement_data.csv")
df = pd.read_csv(raw_path, parse_dates=["PO_Date", "Delivery_Date"])

# === Step 2: Feature Engineering ===
df["delivery_delay_days"] = (df["Delivery_Date"] - df["PO_Date"]).dt.days

df["is_delayed"] = df["Delivery_Status"].apply(
    lambda x: 1 if str(x).strip().lower() == "delayed" else 0
)

df["total_spend"] = df["Quantity"] * df["Unit_Price"]

# === Optional Step: Preview the cleaned data ===
print("\n✅ Sample cleaned data:\n")
print(df.head())

# === Step 3: Save the cleaned data ===
output_path = Path("data/processed/clean_procurement_data.csv")
df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned data saved to: {output_path.resolve()}")
