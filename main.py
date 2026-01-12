#!/usr/bin/env python3
"""
Main entry point for Stock Data Application.

This script provides a command-line interface to fetch Taiwan stock data
and perform linear regression predictions.
"""

import sys
from datetime import datetime
import pandas as pd

from info.TaiwanStockInfo import TaiwanStockInfo
from utils.csvUtils import save_to_csv
from utils.commandLineInterface import CommandLineInterface
from predication.linearRegression import perform_linear_regression


def fetch_stock_data(args) -> None:
    """
    Fetch stock data based on command line arguments.
    
    Args:
        args: Parsed command line arguments
    """
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


def predict_stock_prices(args) -> None:
    """
    Perform linear regression prediction on stock data.
    
    Args:
        args: Parsed command line arguments
    """
    print(f"Performing linear regression analysis on: {args.input}")
    print(f"Output directory: {args.output_dir}")
    
    try:
        results = perform_linear_regression(args.input, args.output_dir)
        print(f"\n=== Analysis Complete ===")
        print(f"Model R² Score: {results['r2_score']:.6f}")
        print(f"Number of predictions: {len(results['predictions'])}")
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error during prediction: {e}")
        sys.exit(1)


def main() -> None:
    """Main entry point for the application."""
    cli = CommandLineInterface()
    args = cli.parse_arguments()
    
    if args.command == "fetch":
        fetch_stock_data(args)
    elif args.command == "predict":
        predict_stock_prices(args)
    else:
        print(f"Error: Unknown command '{args.command}'")
        sys.exit(1)


if __name__ == "__main__":
    main()
