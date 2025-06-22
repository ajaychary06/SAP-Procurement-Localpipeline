# streamlit_app/app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df_forecast = pd.read_csv("data/processed/forecast_output.csv", parse_dates=["ds"])
df_risk = pd.read_csv("data/processed/supplier_risk_scores.csv")
df_procure = pd.read_csv("data/processed/clean_procurement_data.csv")

# Title
st.title("ProcureCast 360: Spend Forecast & Supplier Risk Analytics")

# --- KPIs ---
total_spend = df_procure["total_spend"].sum()
avg_delay = df_procure["delivery_delay_days"].mean()
high_risk_count = df_risk[df_risk["risk_level"] == "High"].shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Spend (USD)", f"${total_spend:,.0f}")
col2.metric("Avg Delivery Delay (days)", f"{avg_delay:.2f}")
col3.metric("High-Risk Vendors", high_risk_count)

st.markdown("---")

# --- Forecast Chart ---
st.subheader("Monthly Spend Forecast")
fig_forecast = px.line(
    df_forecast,
    x="ds", y="yhat",
    title="Forecasted Spend",
    labels={"ds": "Date", "yhat": "Predicted Spend"}
)
st.plotly_chart(fig_forecast)

# --- Risk Table ---
st.subheader("Supplier Risk Scores")
risk_filter = st.selectbox("Show:", ["All Vendors", "Only High-Risk"])
if risk_filter == "Only High-Risk":
    st.dataframe(df_risk[df_risk["risk_level"] == "High"])
else:
    st.dataframe(df_risk)

st.markdown("⚠️ *Model: Isolation Forest based on delivery delays, spend variability & PO count*")
