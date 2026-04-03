"""
analyzer.py - Core Analysis Logic
===================================
This is the brain of the app. It ties together fetching and indicators,
then produces a clean summary dict that both the CLI and web UI can consume.

Keeping this separate means we don't repeat the same logic in main.py and app.py.
"""

from fetch import get_price_history, get_info, get_current_price
from indicators import add_all_indicators


def analyze(symbol, period="6mo"):
    """
    Run a full analysis on a ticker symbol.

    Returns a dict with:
      symbol       -- e.g. 'AAPL'
      name         -- company long name
      sector       -- e.g. 'Technology'
      price        -- latest close price
      pe_ratio     -- trailing P/E ratio (None if not available)
      week52_high  -- 52-week high price
      week52_low   -- 52-week low price
      market_cap   -- market cap in raw dollars
      rsi          -- latest RSI value (float)
      sma20        -- latest 20-day SMA
      sma50        -- latest 50-day SMA
      signal       -- simple string signal based on RSI
      df           -- full price + indicator DataFrame (for charting later)
    """
    info = get_info(symbol)
    df = get_price_history(symbol, period=period)
    df = add_all_indicators(df)

    latest = df.iloc[-1]
    rsi = round(float(latest.get("RSI", 0)), 2)

    # Simple signal based on RSI - you can make this smarter over time
    if rsi < 30:
        signal = "OVERSOLD - possible buy zone"
    elif rsi > 70:
        signal = "OVERBOUGHT - possible sell zone"
    else:
        signal = "NEUTRAL"

    return {
        "symbol": symbol.upper(),
        "name": info.get("longName", "N/A"),
        "sector": info.get("sector", "N/A"),
        "price": get_current_price(symbol),
        "pe_ratio": info.get("trailingPE"),
        "week52_high": info.get("fiftyTwoWeekHigh"),
        "week52_low": info.get("fiftyTwoWeekLow"),
        "market_cap": info.get("marketCap"),
        "rsi": rsi,
        "sma20": round(float(latest.get("SMA_20", 0)), 2),
        "sma50": round(float(latest.get("SMA_50", 0)), 2),
        "signal": signal,
        "df": df,
    }
