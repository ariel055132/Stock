import argparse


class CommandLineInterface:
    """Handles command line argument parsing for the stock data application."""
    
    def parse_arguments(self) -> argparse.Namespace:
        """Parse command line arguments and return the parsed namespace."""
        parser = argparse.ArgumentParser(
            description="Stock Data Application - Fetch and Analyze Stock Data"
        )
        subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")
        
        # Fetch subcommand
        fetch_parser = subparsers.add_parser("fetch", help="Fetch Taiwan stock data")
        fetch_parser.add_argument("stock_id", type=str, help="Stock ID (e.g 0050)")
        fetch_parser.add_argument("start_date", type=str, help="Start date (e.g 2021-09-13)")
        fetch_parser.add_argument("end_date", type=str, nargs="?", default=None, help="End date (YYYY-MM-DD, optional)")
        fetch_parser.add_argument("--output", type=str, default="stock_data.csv", help="Output CSV file name")
        
        # Predict subcommand
        predict_parser = subparsers.add_parser("predict", help="Perform linear regression prediction on stock data")
        predict_parser.add_argument("--input", type=str, required=True, help="Input CSV file path with stock data")
        predict_parser.add_argument("--output-dir", type=str, default="result", help="Output directory for plots and results")
        
        return parser.parse_args()