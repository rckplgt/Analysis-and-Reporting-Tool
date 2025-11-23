import pandas as pd

def load_excel(filepath: str) -> pd.DataFrame:
    """Load Excel file into a DataFrame."""
    try:
        df = pd.read_excel(filepath)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load Excel file: {e}")
