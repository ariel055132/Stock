import pandas as pd

def save_to_csv(data: pd.DataFrame, fileName: str):
    """Save DataFrame to a CSV file.

    :param data: DataFrame to be saved
    :param fileName: Name of the output CSV file
    """
    data.to_csv(fileName, index=False)
    print(f"Data saved to {fileName}")

def load_from_csv(fileName: str) -> pd.DataFrame:
    """Load DataFrame from a CSV file.

    :param fileName: Name of the input CSV file
    :return: Loaded DataFrame
    """
    data = pd.read_csv(fileName, encoding='utf-8')
    print(f"Data loaded from {fileName}")
    return data