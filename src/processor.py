import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans the dataframe and handles missing values.
    """
    df = df.copy()
    df = df.fillna(method='ffill')
    df = df.dropna()
    return df

def add_technical_indicators(df):
    """
    Adds common technical indicators like Moving Averages and RSI.
    """
    df = df.copy()
    
    # Simple Moving Averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    
    # RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Volatility (Rolling Std)
    df['Volatility'] = df['Close'].rolling(window=20).std()
    
    return df
