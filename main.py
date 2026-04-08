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

    # TODO: get the ticker symbol from sys.argv[1] (call it 'symbol')

    # TODO: get the period from sys.argv[2] if it was provided, otherwise default to "6mo"
    #       HINT: ternary -- value = sys.argv[2] if len(sys.argv) > 2 else "6mo"

    # TODO: print a short "Fetching data for AAPL..." message

    # TODO: call analyze(symbol, period=period) and store the result

    # TODO: print the formatted report
    #       The result dict has these keys: name, symbol, sector, price,
    #       market_cap, pe_ratio, week52_high, week52_low, rsi, sma20, sma50, signal
    #       Format it however you like -- below is a suggested layout:
    #
    #       ==========================================
    #         Apple Inc. (AAPL)
    #       ==========================================
    #         Sector:       Technology
    #         Price:        $175.23
    #         Market Cap:   $2.80T
    #         P/E Ratio:    28.5
    #         52W High:     $199.62
    #         52W Low:      $124.17
    #       ------------------------------------------
    #         RSI (14):     44.21
    #         SMA 20:       $172.50
    #         SMA 50:       $168.10
    #       ------------------------------------------
    #         Signal:       NEUTRAL
    #       ==========================================
    #
    #       HINT: "=" * 42 prints a line of 42 equal signs. Use that for separators.
    #       GOOGLE: "Python string multiplication" if that's new to you.
    pass


# This is standard Python boilerplate -- it means "only run main() if this file
# is executed directly, not if it's imported by another file."
# GOOGLE: "Python __name__ == __main__" -- you'll see this everywhere.
if __name__ == "__main__":
    main()
