# 📊 Superstore Sales & Performance Dashboard (Power BI)

[![Power BI](https://img.shields.io/badge/Power_BI-F2C94C?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![SQL](https://img.shields.io/badge/SQL-025E8D?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/excel)
[![Live Demo](https://img.shields.io/badge/Live_Dashboard-Click_Here-brightgreen?style=for-the-badge&logo=google-chrome)](https://surensundharam0627-lang.github.io/Superstore-Sales-Analysis/)

---

## 🌟 Executive Summary & Live Interactive View

🔗 **[Click Here to Access the Live Interactive Dashboard](https://surensundharam0627-lang.github.io/Superstore-Sales-Analysis/)** *(Powered by Power BI Embed & GitHub Pages)*

This data analytics project presents a end-to-end analysis of the **Global Superstore Sales Dataset**. The goal is to provide business executives with actionable insights on profitability, sales performance by region/category, shipping efficiency, and customer purchasing patterns.

---

## 📸 Dashboard Screenshots

### 1. Executive Sales Overview
![Sales Overview](images/overview_dashboard.png)

### 2. Customer & Region Breakdown
![Customer Insights](images/customer_dashboard.png)

---

## 🎯 Business Problem & Key Objectives

1. **Revenue vs. Profitability**: Identify top-performing product categories and sub-categories while pinpointing unprofitable items.
2. **Regional Performance**: Map out sales density across geographic regions to uncover growth opportunities.
3. **Shipping & Operations**: Evaluate order fulfillment times across different shipping modes (`Standard Class`, `Second Class`, `First Class`, `Same Day`).
4. **Customer Segmentation**: Track repeat purchasing behavior and customer lifetime value metrics.

---

## 🔑 Key Insights & Findings

- **Top Revenue Driver**: The **Technology** category generates the highest total revenue, led by **Phones** and **Copiers**.
- **Profit Drainers**: Tables and Bookcases in certain sub-regions exhibit negative profit margins due to excessive discounting (> 20%).
- **Shipping Modes**: `Standard Class` represents 60%+ of total orders but has an average delivery time of 4.5 days.
- **Geographic Hotspots**: The **West & East** regions contribute over 65% of overall net profit.

---

## 🛠️ Data Architecture & Tools Used

- **Data Processing & ETL**: Power Query (M Language) / Excel / Python (Pandas)
- **Data Modeling & DAX**: Power BI Star Schema setup with Time Intelligence calculations
- **SQL Analysis**: Used for exploratory data analysis (EDA) and initial query validation
- **Visualization**: Power BI Desktop (Custom tooltips, bookmarks, interactive drill-throughs)

---

## 📐 Key DAX Measures Used

```dax
// Total Sales Calculation
Total Sales = SUM(Orders[Sales])

// Total Profit Calculation
Total Profit = SUM(Orders[Profit])

// Profit Margin Percentage
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

// Year-over-Year (YoY) Growth
YoY Sales Growth = 
VAR PrevYearSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
RETURN DIVIDE([Total Sales] - PrevYearSales, PrevYearSales, 0)
```

---

## 📁 Repository Structure

```text
├── dataset/
│   └── Superstore_Sales_Data.xlsx       # Raw & cleaned source dataset
├── sql/
│   └── eda_queries.sql                  # Data analysis queries
├── python/
│   └── data_cleaning.py                 # Optional Python ETL script
├── reports/
│   └── Superstore.pbix                  # Power BI Desktop File
├── images/
│   ├── overview_dashboard.png           # High-res screenshot 1
│   └── customer_dashboard.png          # High-res screenshot 2
├── index.html                           # Live GitHub Pages interactive view
└── README.md                            # Project documentation
```

---

## 🚀 How to Run / View This Project Locally

1. **Clone this repository**:
   ```bash
   git clone https://github.com/surensundharam0627-lang/sample.git
   ```
2. **Open Power BI Report**:
   - Double-click `reports/Superstore.pbix` to open it in **Power BI Desktop**.
3. **View Source Data**:
   - Locate the raw dataset in the `dataset/` folder.

---

## 👤 Contact & Portfolio

- **Author**: Data Analyst
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/YOUR_PROFILE)
- **GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
