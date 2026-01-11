# Stock Data Application - Usage Guide

## Overview

This application provides command-line tools to fetch Taiwan stock data from the FinMind API.

## Prerequisites

```bash
# Install dependencies
pip install -r requirements.txt
```

## Command Structure

```bash
python main.py <STOCK_ID> <START_DATE> [END_DATE] [--output FILE]
```

## Available Commands

### 1. Fetch Stock Data

Fetch Taiwan stock price data for a specific stock ID and date range.

**Basic Usage:**
```bash
python main.py <STOCK_ID> <START_DATE> [END_DATE] [--output FILE]
```

**Arguments:**
- `STOCK_ID`: Taiwan stock ID (e.g., 0050, 2330, 2317)
- `START_DATE`: Start date in YYYY-MM-DD format
- `END_DATE`: (Optional) End date in YYYY-MM-DD format (default: today)

**Options:**
- `--output FILE`: Output CSV file path (default: stock_data.csv)

## Examples

### Example 1: Fetch Single Day Data
```bash
python main.py 0050 2024-01-01
```
Fetches 元大台灣50 (0050) stock data for January 1, 2024.

### Example 2: Fetch Date Range Data
```bash
python main.py 2330 2024-01-01 2024-12-31
```
Fetches TSMC (2330) stock data from January 1 to December 31, 2024.

### Example 3: Custom Output Location
```bash
python main.py 2317 2024-01-01 2024-12-31 --output result/hon_hai_2024.csv
```
Fetches Hon Hai (2317) stock data and saves to `result/hon_hai_2024.csv`.

### Example 4: Fetch Data Up to Today
```bash
python main.py 0050 2024-01-01
```
Fetches stock data from January 1, 2024 to today (end date defaults to current date).

## Popular Taiwan Stock IDs

| Stock ID | Company Name | Description |
|----------|--------------|-------------|
| 0050 | 元大台灣50 | Taiwan Top 50 ETF |
| 0056 | 元大高股息 | High Dividend ETF |
| 2330 | 台積電 (TSMC) | Taiwan Semiconductor |
| 2317 | 鴻海 | Hon Hai (Foxconn) |
| 2454 | 聯發科 | MediaTek |
| 2412 | 中華電 | Chunghwa Telecom |

## Output Format

The output CSV file contains the following columns:
- `date`: Trading date
- `stock_id`: Stock ID
- `Trading_Volume`: Trading volume
- `Trading_money`: Trading amount
- `open`: Opening price
- `max`: Highest price
- `min`: Lowest price
- `close`: Closing price
- `spread`: Price spread
- `Trading_turnover`: Trading turnover

## Help Commands

```bash
# Show help
python main.py --help
```

## Troubleshooting

**Error: No data retrieved**
- Check if the stock ID is valid
- Verify the date range (market days only)
- Ensure you have internet connection

**Error: Module not found**
- Make sure you're in the project root directory
- Verify all dependencies are installed: `pip install -r requirements.txt`

## Direct Module Execution (Alternative)

You can also run the TaiwanStockInfo module directly:

```bash
python info/TaiwanStockInfo.py 0050 2024-01-01 2024-12-31 --output result/data.csv
```

This bypasses the main.py entry point and calls the module directly.
