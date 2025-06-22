# scripts/risk_scoring.py

import pandas as pd
from sklearn.ensemble import IsolationForest
from pathlib import Path

# === Step 1: Load cleaned procurement data ===
df = pd.read_csv("data/processed/clean_procurement_data.csv", parse_dates=["PO_Date"])

# === Step 2: Aggregate supplier-level features ===
supplier_metrics = df.groupby("Vendor_ID").agg({
    "delivery_delay_days": "mean",
    "is_delayed": "mean",
    "total_spend": ["mean", "std", "count"]
}).reset_index()

# Flatten column names
supplier_metrics.columns = [
    "Vendor_ID", "avg_delay", "delay_rate", "avg_spend", "spend_std", "po_count"
]

# Fill NA values
supplier_metrics.fillna(0, inplace=True)

# === Step 3: Train Isolation Forest ===
features = supplier_metrics.drop(columns=["Vendor_ID"])
model = IsolationForest(contamination=0.2, random_state=42)
supplier_metrics["anomaly_flag"] = model.fit_predict(features)

# === Step 4: Convert -1 to 'High' Risk ===
supplier_metrics["risk_level"] = supplier_metrics["anomaly_flag"].apply(
    lambda x: "High" if x == -1 else "Low"
)
supplier_metrics.drop(columns=["anomaly_flag"], inplace=True)

# === Step 5: Save output ===
output_path = Path("data/processed/supplier_risk_scores.csv")
supplier_metrics.to_csv(output_path, index=False)

print(f"✅ Risk scores saved to {output_path.resolve()}")
print(supplier_metrics.head())
