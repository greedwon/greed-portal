# Stock Analyzer

A personal stock analysis tool with a CLI and a Flask web UI.
Built to be continuously expanded.

## Features (starter set)
- Pull live price, volume, and fundamentals for any ticker
- Simple moving average (SMA 20, SMA 50) calculations
- RSI (Relative Strength Index) with a basic buy/sell signal
- CLI for quick terminal lookups
- Web UI for a nicer view

## Setup

```bash
pip install -r requirements.txt
```

## Run the CLI
```bash
python3 main.py AAPL
python3 main.py TSLA 1y
```

## Run the Web UI
```bash
python3 app.py
```
Then open http://localhost:5000 in your browser.

To enable auto-reload during development:
```bash
DEBUG=true python3 app.py
```

## Project Structure
```
stock-analyzer/
  main.py          -- CLI entry point
  app.py           -- Flask web app
  analyzer.py      -- core analysis logic (shared by CLI and web)
  fetch.py         -- data fetching wrapper around yfinance
  indicators.py    -- technical indicators (SMA, RSI, etc.)
  data/            -- cached data files (gitignored)
  templates/       -- HTML templates for the web UI
  static/css/      -- stylesheet
  static/js/       -- JavaScript (Chart.js etc. later)
```
