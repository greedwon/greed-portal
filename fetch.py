"""
fetch.py - Data Fetching
========================
All the code that actually goes out and grabs stock data lives here.
We use yfinance which pulls from Yahoo Finance - free and no API key needed.

If you ever want to swap in a different data source (Alpaca, Polygon.io, etc.)
you only need to change this one file.
"""

import yfinance as yf


def get_ticker(symbol):
    """
    Returns a yfinance Ticker object for the given symbol.
    Think of this as opening a dossier on a company.
    """
    return yf.Ticker(symbol.upper())


def get_price_history(symbol, period="6mo", interval="1d"):
    """
    Pull OHLCV (Open, High, Low, Close, Volume) price history.

    period options:   1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    interval options: 1m, 5m, 15m, 1h, 1d, 1wk, 1mo

    Returns a pandas DataFrame.
    """
    ticker = get_ticker(symbol)
    df = ticker.history(period=period, interval=interval)
    return df


def get_info(symbol):
    """
    Pull basic company info and fundamentals.
    Returns a dict with keys like: longName, sector, marketCap,
    trailingPE, dividendYield, fiftyTwoWeekHigh, fiftyTwoWeekLow, etc.
    """
    ticker = get_ticker(symbol)
    return ticker.info


def get_current_price(symbol):
    """
    Get just the latest closing price as a float.
    """
    df = get_price_history(symbol, period="5d", interval="1d")
    if df.empty:
        return None
    return round(df["Close"].iloc[-1], 2)
