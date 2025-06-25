# 🚀 ProcureCast 360: Predictive Spend Forecasting & Supplier Risk Analytics

**ProcureCast 360** is a local, end-to-end data analytics pipeline designed to forecast procurement spend and detect high-risk suppliers using real-world SAP-style procurement data.

---

## 🎯 Project Objective

- Forecast future spend by vendor or material category.
- Score suppliers based on delays, volatility, and behavior.
- Deliver insights via an interactive **Power BI Dashboard** and a **Streamlit app**.

---

## 🧩 Tech Stack

| Layer         | Tools Used                                      |
|---------------|-------------------------------------------------|
| Data Source   | SAP-style procurement CSV                       |
| Data Cleaning | Python (pandas, pathlib)                        |
| ML Models     | Prophet, Scikit-learn (Isolation Forest)        |
| Dashboard     | Power BI Desktop                                |
| UI            | Streamlit                                       |

---

## 🗂️ Folder Structure

ProcureCast360/

├── data/

│ ├── raw/ # input CSVs

│ └── processed/ # output/engineered files

├── scripts/ # cleaning, modeling

├── streamlit_app/ # local web UI

├── dashboard/PowerBI/ # .pbix & .pdf exports

├── models/ # optional model files

├── pipeline_diagram.png # visual flow

├── README.md

├── requirements.txt


---




## 🧠 Key Features

- `data_cleaning.py` → Cleans raw SAP-style procurement data
- `forecast_spend.py` → Uses Prophet to forecast monthly spend
- `risk_scoring.py` → Applies Isolation Forest to flag risky suppliers
- `streamlit_app/app.py` → Browser-based summary of KPIs and results
- Power BI Dashboard → Visualizes spend trends and supplier risk

---

## 📊 Dashboard & App

- **Power BI Dashboard**:  
  `dashboard/PowerBI/ProcureCast_Dashboard.pbix`  
  Exportable to `.pdf` for presentation.

- **Streamlit App**:  
  Launch with:
  ```bash
  streamlit run streamlit_app/app.py
  ```

## 🛠️ Installation

``` bash
git clone https://github.com/ajaychary06/ProcureCast360.git
cd ProcureCast360
pip install -r requirements.txt
```

## 📁 Run the Pipeline
#### Step 1: Clean data

``` bash
python scripts/data_cleaning.py
```

#### Step 2: Forecast spend

``` bash
python scripts/forecast_spend.py
```

#### Step 3: Score supplier risk
``` bash
python scripts/risk_scoring.py
```

#### Step 4: Run Streamlit app (optional)
``` bash
streamlit run streamlit_app/app.py
```


## 📌 Outputs

| File                         | Purpose                        |
| ---------------------------- | ------------------------------ |
| `clean_procurement_data.csv` | Cleaned SAP-style data         |
| `forecast_output.csv`        | Monthly spend forecast         |
| `supplier_risk_scores.csv`   | Risk scores by supplier        |
| `ProcureCast_Dashboard.pbix` | Power BI interactive dashboard |


## 👤 Author

**Ajaychary Kandukuri** 

🎓 Master’s Student in Data Science 

🔗 [Portfolio](https://ajaychary06.github.io/Portfolio/) 

🐍 [GitHub](https://github.com/ajaychary06) 

💼 [LinkedIn](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a/)”

[Gmail](ajaycharykandukuri06@gmail.com)


## ⭐ Project Highlights

✅ Real-world data pipeline simulation without cloud dependencies

✅ Forecasting using Prophet with time-series tuning

✅ Isolation Forest to detect risky supplier behavior

✅ Dual frontend: Power BI & Streamlit


