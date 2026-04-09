"""
indicators.py - Technical Indicators
=====================================
Functions that take a price DataFrame and return it with new columns added.
These are the building blocks of technical analysis.

All functions expect a pandas DataFrame with at least a 'Close' column
(the format returned by fetch.get_price_history).

GOOGLE TIP: "pandas DataFrame" -- the whole file revolves around this.
Think of a DataFrame like a spreadsheet where each row is a day and
each column is a piece of data (Open, High, Low, Close, Volume).
"""

import pandas as pd


def simple_moving_average(df, window=20):
    """
    SMA - Simple Moving Average.
    Smooths out price noise by averaging the last N closing prices.
    Common windows: 20 (short-term), 50 (medium), 200 (long-term trend).

    Returns the DataFrame with a new column added: 'SMA_{window}'.
    Example: window=20 adds a column called 'SMA_20'.
    """
    # copies df, pulls window variable to determine name and window length, computes rolling average closing prices over window length.
    df = df.copy()
    column_name = f"SMA_{window}"
    df[column_name] = df["Close"].rolling(window=window).mean()
    return df


def relative_strength_index(df, window=14):
    """
    Step 1 - Get daily price changes:
        delta = df["Close"].diff()
        GOOGLE: "pandas diff() method"

    Step 2 - Split changes into gains and losses:
        gain = delta.clip(lower=0)   # negative changes become 0
        loss = -delta.clip(upper=0)  # positive changes become 0, then flip sign
        GOOGLE: "pandas clip method"

    Step 3 - Rolling average of gains and losses over the window:
        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

    Step 4 - Calculate Relative Strength:
        rs = avg_gain / avg_loss

    Step 5 - Convert to RSI scale (0-100):
        RSI = 100 - (100 / (1 + rs))

    Step 6 - Assign to df["RSI"] and return df.
    """
    # TODO: copy df
    df = df.copy()
    # TODO: calculate delta (daily price changes)
    delta = df["Close"].diff()
    # TODO: split into gain and loss series
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    # TODO: calculate rolling averages for both
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    # TODO: calculate rs (relative strength)
    rs = avg_gain / avg_loss
    # TODO: calculate RSI and assign to df["RSI"]
    df["RSI"] = 100 - (100 / (1 + rs))
    # TODO: return df
    return df


def bollinger_bands(df, window=20, num_std=2):
    """
    Bollinger Bands - a volatility indicator.
    Three lines: a middle SMA, an upper band, and a lower band.
    The bands widen when price is volatile and tighten when it's quiet.

    Returns df with three new columns:
        'BB_middle'  -- the SMA (same as SMA_20)
        'BB_upper'   -- middle + (num_std * rolling standard deviation)
        'BB_lower'   -- middle - (num_std * rolling standard deviation)
    """
    # copy df
    df = df.copy()
    #  calculate the rolling mean (middle band)
    df["BB_middle"] = df["Close"].rolling(window=window).mean()
    #  calculate the rolling standard deviation
    std = df["Close"].rolling(window=window).std()
    #  calculate upper band (middle + num_std * std)
    df["BB_upper"] = df["BB_middle"] + (num_std * std)
    #  calculate lower band (middle - num_std * std)
    df["BB_lower"] = df["BB_middle"] - (num_std * std)
    return df


def add_all_indicators(df):
    """
    Convenience function: adds all indicators to the DataFrame at once.
    Call this when you want a fully loaded dataset ready to analyze.

    """
    #  call simple_moving_average with window=20
    simple_moving_average(df, window=20)
    #  call simple_moving_average with window=50
    simple_moving_average(df, window=50)
    #  call relative_strength_index
    relative_strength_index(df)
    #  call bollinger_bands
    bollinger_bands(df)
    #  return df
    return df
