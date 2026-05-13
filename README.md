# 🪙 Crypto Time Series AI

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Prophet](https://img.shields.io/badge/Forecasting-Prophet-blueviolet?style=for-the-badge)]()

An advanced cryptocurrency analysis and forecasting platform that leverages **Time Series Analysis**, **Machine Learning**, and **NLP** to provide actionable insights for traders and researchers.

---

## 🚀 Key Features

### 1. 📊 Real-Time Data Collection
- Fetches live and historical price data for major cryptocurrencies (BTC, ETH, SOL, etc.) using **Yahoo Finance** and **CoinGecko** integrations.
- Supports customizable timeframes (Daily, Hourly) and historical periods.

### 2. 📈 Technical Indicators & Preprocessing
- Automated cleaning and processing of financial datasets.
- Instant calculation of core technical indicators:
  - **Moving Averages** (SMA 20, SMA 50)
  - **Relative Strength Index (RSI)**
  - **Rolling Volatility**

### 3. 🔮 AI-Driven Price Forecasting
- Implements the **Facebook Prophet** model for robust time series prediction.
- Generates future price trajectories with confidence intervals for up to 90 days.
- Designed to handle seasonality and market holidays automatically.

### 4. 📰 Sentiment & Volatility Analysis
- **NLP Sentiment Engine**: Analyzes market news and snippets to gauge "Bullish" vs "Bearish" sentiment.
- **Volatility Tracking**: Visualizes market risk using area charts.

---

## 🏗️ Project Structure

```text
crypto-time-series/
├── src/
│   ├── collector.py    # Data fetching logic (yfinance)
│   ├── processor.py    # Cleaning & technical indicators
│   ├── forecaster.py   # Prophet forecasting model
│   └── sentiment.py    # NLP sentiment analysis
├── data/               # Local data storage
├── app.py              # Main Streamlit Dashboard
└── requirements.txt    # Dependency list
```

---

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.9 or higher

### Setup
1. **Navigate to the project folder**:
   ```bash
   cd crypto-time-series
   ```
2. **Create a virtual environment** (Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```

---

## 📄 License
This project is part of the Amdox Internship portfolio and is licensed under the MIT License.

---
