"""
app.py - Flask Web App
=======================
Serves the stock analyzer as a browser UI.

Run with: python3 app.py
Then open http://localhost:5000 in your browser.
"""

import os
import re
from flask import Flask, render_template, request
from analyzer import analyze

app = Flask(__name__)

# Allowed period values - we whitelist these so random input can't be passed to yfinance
VALID_PERIODS = {"1mo", "3mo", "6mo", "1y", "2y", "5y"}


def format_market_cap(cap):
    """Format a raw market cap number into something readable like '2.80T'."""
    if cap is None:
        return "N/A"
    if cap >= 1e12:
        return f"${cap / 1e12:.2f}T"
    if cap >= 1e9:
        return f"${cap / 1e9:.2f}B"
    if cap >= 1e6:
        return f"${cap / 1e6:.2f}M"
    return f"${cap:,.0f}"


@app.route("/")
def index():
    """Home page - shows the search form."""
    return render_template("index.html")


@app.route("/analyze")
def analyze_stock():
    """
    Handles the analyze request from the search form.
    URL: /analyze?symbol=AAPL&period=6mo
    """
    symbol = request.args.get("symbol", "").strip().upper()
    period = request.args.get("period", "6mo")

    if not symbol:
        return render_template("index.html", error="Please enter a ticker symbol.")

    # Only allow letters, numbers, dots and hyphens (covers AAPL, RY.TO, BRK-B etc.)
    if not re.match(r'^[A-Z0-9.\-]{1,12}$', symbol):
        return render_template("index.html", error="Invalid ticker format.")

    # Whitelist period to prevent arbitrary values reaching yfinance
    if period not in VALID_PERIODS:
        period = "6mo"

    try:
        result = analyze(symbol, period=period)
        # Format market cap before passing to the template
        result["market_cap"] = format_market_cap(result["market_cap"])
        # Remove the DataFrame - it's not needed in the template
        result.pop("df")
        return render_template("result.html", data=result, period=period)
    except Exception as e:
        error = f"Could not fetch data for '{symbol.upper()}'. Make sure it's a valid ticker. ({e})"
        return render_template("index.html", error=error)


if __name__ == "__main__":
    # Read debug mode from environment variable so it's never accidentally on in production
    # To enable during development: DEBUG=true python3 app.py
    debug = os.environ.get("DEBUG", "false").lower() == "true"
    app.run(debug=debug)
