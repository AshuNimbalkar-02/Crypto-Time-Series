import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.collector import fetch_crypto_data, get_realtime_price
from src.processor import clean_data, add_technical_indicators
from src.forecaster import forecast_with_prophet
from src.sentiment import get_crypto_news_sentiment
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Crypto Time Series AI", page_icon="📈", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .stAlert { background-color: #161b22; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 Cryptocurrency Time Series Analysis & Forecasting")
st.markdown("Leveraging Data Science and ML to predict the future of decentralized finance.")

# Sidebar Controls
st.sidebar.header("Configuration")
symbol = st.sidebar.selectbox("Select Cryptocurrency", ["BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "ADA-USD"])
period = st.sidebar.selectbox("History Period", ["6mo", "1y", "2y", "5y"])
forecast_days = st.sidebar.slider("Forecast Horizon (Days)", 7, 90, 30)

# Data Collection
with st.spinner("Fetching market data..."):
    raw_df = fetch_crypto_data(symbol, period)
    current_price = get_realtime_price(symbol)

if raw_df is not None:
    # Processing
    df = clean_data(raw_df)
    df = add_technical_indicators(df)
    
    # Header Metrics
    col1, col2, col3, col4 = st.columns(4)
    price_change = df['Close'].iloc[-1] - df['Close'].iloc[-2]
    col1.metric("Current Price", f"${current_price:,.2f}", f"{price_change:,.2f}")
    col2.metric("24h High", f"${df['High'].iloc[-1]:,.2f}")
    col3.metric("RSI (14)", f"{df['RSI'].iloc[-1]:.2f}")
    
    sentiment_score, news = get_crypto_news_sentiment(symbol.split('-')[0])
    sentiment_label = "Bullish" if sentiment_score > 0 else "Bearish"
    col4.metric("Sentiment Index", sentiment_label, f"{sentiment_score:.2f}")

    # Main Chart
    st.subheader(f"{symbol} Price & Technical Indicators")
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name="Price"))
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], name="SMA 20", line=dict(color='orange', width=1)))
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], name="SMA 50", line=dict(color='cyan', width=1)))
    
    fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False, height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Forecasting Section
    st.divider()
    st.subheader(f"🚀 {forecast_days}-Day Price Prediction (Prophet Model)")
    
    with st.spinner("Generating AI forecast..."):
        forecast, model = forecast_with_prophet(df, periods=forecast_days)
        
        fig_forecast = go.Figure()
        # Actual
        fig_forecast.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Historical Price", line=dict(color='#3b82f6')))
        # Forecast
        forecast['ds'] = pd.to_datetime(forecast['ds']).dt.tz_localize(None)
        last_date = pd.to_datetime(df.index).tz_localize(None)[-1]
        forecast_filtered = forecast[forecast['ds'] > last_date]
        fig_forecast.add_trace(go.Scatter(x=forecast_filtered['ds'], y=forecast_filtered['yhat'], name="Predicted Price", line=dict(color='#10b981', dash='dash')))
        # Confidence Interval
        fig_forecast.add_trace(go.Scatter(
            x=pd.concat([forecast_filtered['ds'], forecast_filtered['ds'][::-1]]),
            y=pd.concat([forecast_filtered['yhat_upper'], forecast_filtered['yhat_lower'][::-1]]),
            fill='toself',
            fillcolor='rgba(16, 185, 129, 0.1)',
            line=dict(color='rgba(255,255,255,0)'),
            name="Confidence Interval"
        ))
        
        fig_forecast.update_layout(template="plotly_dark", height=500)
        st.plotly_chart(fig_forecast, use_container_width=True)

    # News & Sentiment
    st.divider()
    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("📰 Recent Sentiment Analysis")
        for n in news:
            st.info(n)
    with c2:
        st.subheader("📊 Volatility Analysis")
        st.area_chart(df['Volatility'])

else:
    st.error("Could not fetch data for the selected symbol. Please try again later.")
