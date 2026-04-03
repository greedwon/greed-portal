"""
indicators.py - Technical Indicators
=====================================
Functions that take a price DataFrame and return calculated indicator values.
These are the building blocks of technical analysis.

All functions expect a pandas DataFrame with at least a 'Close' column
(the format returned by fetch.get_price_history).
"""

import pandas as pd


def simple_moving_average(df, window=20):
    """
    SMA - Simple Moving Average.
    Smooths out price noise by averaging the last N closing prices.
    Common windows: 20 (short-term), 50 (medium), 200 (long-term trend).

    Returns the DataFrame with a new column added: 'SMA_{window}'.
    """
    col = f"SMA_{window}"
    df = df.copy()
    df[col] = df["Close"].rolling(window=window).mean()
    return df


def relative_strength_index(df, window=14):
    """
    RSI - Relative Strength Index (0-100 scale).
    Measures whether a stock is overbought (>70) or oversold (<30).
    Most traders treat 30 as a potential buy signal, 70 as a potential sell.

    Returns the DataFrame with a new column: 'RSI'.
    """
    df = df.copy()
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df


def add_all_indicators(df):
    """
    Convenience: adds SMA20, SMA50, and RSI14 all at once.
    Call this when you want a fully loaded dataset ready to analyze.
    """
    df = simple_moving_average(df, window=20)
    df = simple_moving_average(df, window=50)
    df = relative_strength_index(df)
    return df
