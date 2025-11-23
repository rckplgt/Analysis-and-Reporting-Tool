import pandas as pd

def generate_summary(df: pd.DataFrame) -> dict:
    """Return dictionary of summary outputs."""
    summary = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "numeric_summary": df.describe(include='number').round(2),
        "categorical_summary": df.describe(include='object')
    }
    return summary

def get_user_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ask the user which columns to group by, which columns to summarize,
    and which type of summary to compute. Returns a summary DataFrame.
    """
    # Show available columns
    print("Columns available in the dataset:")
    print(list(df.columns))

    # Ask for grouping columns
    group_cols = input("Enter columns to group by (comma-separated): ").split(",")
    group_cols = [col.strip() for col in group_cols]

    # Ask for columns to summarize
    summary_cols = input("Enter columns to summarize (comma-separated): ").split(",")
    summary_cols = [col.strip() for col in summary_cols]

    # Ask for summary type
    print("Summary types available: mean, sum, count, min, max, describe")
    summary_type = input("Enter summary type: ").strip().lower()

    # Validate columns
    for col in group_cols + summary_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the dataset.")

    # Group the data
    grouped = df.groupby(group_cols)[summary_cols]

    # Compute summary
    if summary_type == "mean":
        summary_df = grouped.mean()
    elif summary_type == "sum":
        summary_df = grouped.sum()
    elif summary_type == "count":
        summary_df = grouped.count()
    elif summary_type == "min":
        summary_df = grouped.min()
    elif summary_type == "max":
        summary_df = grouped.max()
    elif summary_type == "describe":
        summary_df = grouped.describe().round(2)
    else:
        raise ValueError("Invalid summary type selected.")

    # Reset index so group columns become normal columns
    summary_df = summary_df.reset_index()

    return summary_df