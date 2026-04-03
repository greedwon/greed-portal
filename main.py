"""
main.py - CLI Entry Point
==========================
Run from the terminal to quickly analyze a stock.

Usage:
    python3 main.py AAPL
    python3 main.py TSLA 1y
    python3 main.py SPY 3mo
"""

import sys
from analyzer import analyze


def format_market_cap(cap):
    """Turn a raw number like 2800000000000 into '2.80T' for readability."""
    if cap is None:
        return "N/A"
    if cap >= 1e12:
        return f"${cap / 1e12:.2f}T"
    if cap >= 1e9:
        return f"${cap / 1e9:.2f}B"
    if cap >= 1e6:
        return f"${cap / 1e6:.2f}M"
    return f"${cap:,.0f}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <TICKER> [period]")
        print("  period options: 1mo 3mo 6mo 1y 2y  (default: 6mo)")
        sys.exit(1)

    symbol = sys.argv[1]
    period = sys.argv[2] if len(sys.argv) > 2 else "6mo"

    print(f"\nFetching data for {symbol.upper()}...")
    result = analyze(symbol, period=period)

    print("=" * 42)
    print(f"  {result['name']} ({result['symbol']})")
    print("=" * 42)
    print(f"  Sector:       {result['sector']}")
    print(f"  Price:        ${result['price']}")
    print(f"  Market Cap:   {format_market_cap(result['market_cap'])}")
    print(f"  P/E Ratio:    {result['pe_ratio'] or 'N/A'}")
    print(f"  52W High:     ${result['week52_high']}")
    print(f"  52W Low:      ${result['week52_low']}")
    print("-" * 42)
    print(f"  RSI (14):     {result['rsi']}")
    print(f"  SMA 20:       ${result['sma20']}")
    print(f"  SMA 50:       ${result['sma50']}")
    print("-" * 42)
    print(f"  Signal:       {result['signal']}")
    print("=" * 42)


main()
