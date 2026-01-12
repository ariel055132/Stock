import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from utils.csvUtils import save_to_csv, load_from_csv
import matplotlib.pyplot as plt


def perform_linear_regression(input_csv: str, output_dir: str = "result") -> dict:
    """
    Perform linear regression analysis on stock data.
    
    Args:
        input_csv: Path to input CSV file with stock data
        output_dir: Directory to save output plots and results
        
    Returns:
        Dictionary with prediction results including R² score, coefficients, and intercept
        
    Raises:
        ValueError: If required columns are missing from the CSV
        FileNotFoundError: If input CSV file doesn't exist
    """
    # Validate required columns
    required_columns = ['Open', 'High', 'Low', 'Volume', 'Close']
    
    # Load data
    df = load_from_csv(input_csv)
    print(f"\nData loaded from {input_csv}")
    print(df.head(5))
    
    # Check for required columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}. Required: {required_columns}")
    
    # Data preprocessing
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df.Date)
    
    # Drop Adj Close if exists
    if 'Adj Close' in df.columns:
        df.drop('Adj Close', axis=1, inplace=True)
    
    df['Volume'] = df['Volume'].astype(float)
    
    # Remove rows with NaN or infinite values
    df_new = df[np.isfinite(df).all(1)]
    
    print(f"\nData shape after cleaning: {df_new.shape}")
    print(f"Null values: {df_new.isnull().sum().sum()}")
    
    # Prepare features and target
    x = df_new[['Open', 'High', 'Low', 'Volume']]
    y = df_new['Close']
    
    # Split data
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    
    # Train model
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    
    # Make predictions
    predicted = regressor.predict(x_test)
    
    # Calculate metrics
    r2_score = regressor.score(x_test, y_test)
    
    print(f"\n=== Linear Regression Results ===")
    print(f"Coefficients: {regressor.coef_}")
    print(f"Intercept: {regressor.intercept_}")
    print(f"R² Score: {r2_score:.6f}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create comparison DataFrame
    dfr = pd.DataFrame({'Actual': y_test, 'Predicted': predicted})
    
    # Plot actual closing prices
    lst = [i for i in range(0, len(dfr.Actual))]
    ak = dfr.head(len(dfr.Actual))
    aka = ak.sort_values("Actual")
    
    plt.figure(figsize=(12, 6))
    plt.plot(lst, aka['Actual'].values, label='Actual', color='blue')
    plt.xlabel("Time")
    plt.ylabel("Stock Closing Price")
    plt.title("Actual Closing Price")
    plt.legend()
    actual_plot_path = os.path.join(output_dir, 'actual_closing_price.png')
    plt.savefig(actual_plot_path)
    plt.close()
    print(f"\nActual price plot saved to: {actual_plot_path}")
    
    # Plot predicted closing prices
    aak = ak.sort_values("Predicted")
    plt.figure(figsize=(12, 6))
    plt.plot(lst, aak['Predicted'].values, label='Predicted', color='orange')
    plt.xlabel("Time")
    plt.ylabel("Stock Closing Price")
    plt.title("Predicted Closing Price")
    plt.legend()
    predicted_plot_path = os.path.join(output_dir, 'predicted_closing_price.png')
    plt.savefig(predicted_plot_path)
    plt.close()
    print(f"Predicted price plot saved to: {predicted_plot_path}")
    
    # Save comparison results
    comparison_csv_path = os.path.join(output_dir, 'prediction_comparison.csv')
    dfr.to_csv(comparison_csv_path, index=False)
    print(f"Prediction comparison saved to: {comparison_csv_path}")
    
    return {
        'r2_score': r2_score,
        'coefficients': regressor.coef_.tolist(),
        'intercept': regressor.intercept_,
        'predictions': predicted.tolist(),
        'actual_values': y_test.tolist()
    }


if __name__ == "__main__":
    # For standalone execution
    perform_linear_regression('result/TSLA.csv', 'result')