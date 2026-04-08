"""
analyzer.py - Core Analysis Logic
===================================
This is the brain of the app. It ties together fetching and indicators,
then produces a clean summary dict that both the CLI and web UI can consume.

Keeping this separate means we don't repeat the same logic in main.py and app.py.
That principle is called "separation of concerns" -- GOOGLE that term, it's worth knowing.
"""

from fetch import get_price_history, get_info, get_current_price
from indicators import add_all_indicators


def generate_signal(rsi, sma20, sma50):
    """
    Takes indicator values and returns a human-readable signal string.

    Right now the logic is simple -- just RSI thresholds.
    Over time you can make this smarter by combining multiple indicators.

    Returns a string like "OVERSOLD - possible buy zone" or "NEUTRAL".

    HINTS:
    - RSI below 30 is generally considered oversold (possibly undervalued)
    - RSI above 70 is generally considered overbought (possibly overvalued)
    - Between 30-70 is neutral
    - GOOGLE: "RSI trading signals" for more context
    - Later you could add: if sma20 > sma50 it's called a "golden cross" (bullish)
        and if sma20 < sma50 it's a "death cross" (bearish) -- GOOGLE both terms

    TODO: replace 'pass' and the placeholder return with your logic.
    Use if/elif/else -- you know how to do this from boot.dev.
    """
    # TODO: if rsi < 30, return an oversold message
    # TODO: elif rsi > 70, return an overbought message
    # TODO: else return "NEUTRAL"
    pass


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
      signal       -- a string signal from generate_signal()
      df           -- the full DataFrame with all indicators (for charting later)

    HINTS:
    - df.iloc[-1] gets the last row of the DataFrame (most recent day's data).
        GOOGLE: "pandas iloc" -- it's the main way to grab rows by position.
    - latest.get("RSI", 0) safely gets the RSI value, returning 0 if it's missing.
        This is dict-style access -- DataFrames support it too.
    - round(float(value), 2) is just cleanup: convert to float, round to 2 decimals.
    - info.get("longName", "N/A") does the same for the company info dict.

    TODO: the function body is stubbed out for you below. Fill in the blanks.
    """
    # These three lines are done -- they fetch the raw data. Don't touch them.
    info = get_info(symbol)
    df = get_price_history(symbol, period=period)
    df = add_all_indicators(df)

    # TODO: get the last row of df (call it 'latest')

    # TODO: get the RSI value from latest -- round it to 2 decimal places
    #       HINT: round(float(latest.get("RSI", 0)), 2)

    # TODO: get sma20 from latest -- same pattern as rsi above (key is "SMA_20")

    # TODO: get sma50 from latest (key is "SMA_50")

    # TODO: call generate_signal(rsi, sma20, sma50) to get the signal string

    # TODO: return a dict with all the fields listed in the docstring above
    #       HINT: use info.get("keyName", "N/A") for company info fields
    #       The yfinance keys are: longName, sector, trailingPE,
    #       fiftyTwoWeekHigh, fiftyTwoWeekLow, marketCap
    pass
