#!/usr/bin/env python3
"""
Main entry point for Stock Data Application.

This script provides a command-line interface to fetch Taiwan stock data.
"""

import sys
from datetime import datetime
import pandas as pd

from info.TaiwanStockInfo import TaiwanStockInfo
from utils.csvUtils import save_to_csv
from utils.commandLineInterface import CommandLineInterface


def main() -> None:
    """Main entry point for the application."""
    # Use the existing CommandLineInterface from utils
    cli = CommandLineInterface()
    args = cli.parse_arguments()
    
    print(f"Fetching stock data for {args.stock_id}...")
    print(f"Start date: {args.start_date}")
    
    if args.end_date:
        print(f"End date: {args.end_date}")
    else:
        print(f"End date: {datetime.now().strftime('%Y-%m-%d')} (today)")
    
    # Fetch stock data
    stock_info = TaiwanStockInfo()
    stock_data = stock_info.get_stock_deal_info(
        args.stock_id,
        args.start_date,
        args.end_date
    )
    
    if not stock_data:
        print("Error: No data retrieved. Please check your stock ID and date range.")
        sys.exit(1)
    
    # Convert to DataFrame and save
    df = pd.DataFrame(stock_data)
    save_to_csv(df, args.output)
    print(f"Successfully fetched {len(df)} records.")


if __name__ == "__main__":
    main()
