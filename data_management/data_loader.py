import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Simple cleaning: drop empty rows and trim column names."""
    df = df.dropna(how='all')
    df.columns = [c.strip() for c in df.columns]
    return df
