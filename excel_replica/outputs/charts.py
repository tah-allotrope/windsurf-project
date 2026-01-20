"""Optional chart generation for reports."""

import pandas as pd


def build_charts(df: pd.DataFrame, output_dir: str) -> None:
    """Generate charts for report visuals."""
    raise NotImplementedError("Implement chart generation.")
