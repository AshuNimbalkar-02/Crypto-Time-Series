import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_crypto_data(symbol='BTC-USD', period='1y', interval='1d'):
    """
    Fetches historical cryptocurrency data from Yahoo Finance.
    """
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def get_realtime_price(symbol='BTC-USD'):
    """
    Fetches the current price of a cryptocurrency.
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.fast_info
        return data['last_price']
    except:
        return None
