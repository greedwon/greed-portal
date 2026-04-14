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
    """
    Turn a raw number like 2800000000000 into '2.80T' for readability.
    This is already done for you -- read it and make sure you understand it.

    GOOGLE: "Python f-strings" and "scientific notation Python" if any of it is fuzzy.
    1e12 is just Python's way of writing 1,000,000,000,000 (one trillion).
    """
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
    """
    The CLI entry point. Reads args from the terminal, runs the analysis,
    and prints a formatted report.

    sys.argv is the list of words you typed in the terminal.
    sys.argv[0] is always the script name ("main.py").
    sys.argv[1] would be the ticker ("AAPL"), sys.argv[2] the period ("1y"), etc.
    GOOGLE: "Python sys.argv" for a quick explainer.

    HINT: len(sys.argv) tells you how many arguments were passed.
    If it's less than 2, the user forgot to give a ticker -- print help and exit.
    sys.exit(1) exits with an error code (1 = error, 0 = success).
    """
    # TODO: check if a ticker was provided (len(sys.argv) < 2), print usage and exit if not
    if len(sys.argv) < 2:
        print("Usage: python main.py <ticker> [period]")
        sys.exit(1)

    # TODO: get the ticker symbol from sys.argv[1] (call it 'symbol')
    symbol = sys.argv[1]

    # TODO: get the period from sys.argv[2] if it was provided, otherwise default to "6mo"
    #       HINT: ternary -- value = sys.argv[2] if len(sys.argv) > 2 else "6mo"
    period = sys.argv[2] if len(sys.argv) > 2 else "6mo"

    # TODO: print a short "Fetching data for AAPL..." message
    print(f"Fetching data for {symbol}...")

    # TODO: call analyze(symbol, period=period) and store the result
    result = analyze(symbol, period=period)

    # TODO: print the formatted report
    #       The result dict has these keys: name, symbol, sector, price,
    #       market_cap, pe_ratio, week52_high, week52_low, rsi, sma20, sma50, signal

    print(f"{'=' * 42}\n  {result['name']} ({result['symbol']})\n{'=' * 42}")
    print(f"  Sector:       {result['sector']}")
    print(f"  Price:        ${result['price']:.2f}")
    print(f"  Market Cap:   ${result['market_cap']:.2f}T")
    print(f"  P/E Ratio:    {result['pe_ratio']:.1f}")
    print(f"  52W High:     ${result['week52_high']:.2f}")
    print(f"  52W Low:      ${result['week52_low']:.2f}")
    print(f"{'=' * 42}")
    print(f"  RSI (14):     {result['rsi']:.2f}")
    print(f"  SMA 20:       ${result['sma20']:.2f}")
    print(f"  SMA 50:       ${result['sma50']:.2f}")
    print(f"{'=' * 42}")
    print(f"  Signal:       {result['signal']}")
    print(f"{'=' * 42}")


# This is standard Python boilerplate -- it means "only run main() if this file
# is executed directly, not if it's imported by another file."
# GOOGLE: "Python __name__ == __main__" -- you'll see this everywhere.
if __name__ == "__main__":
    main()
