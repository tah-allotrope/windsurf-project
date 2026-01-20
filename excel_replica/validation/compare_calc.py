"""Compare Calc sheet outputs against Excel truth."""

from typing import Dict

import pandas as pd


def compare_calc(model_df: pd.DataFrame, excel_df: pd.DataFrame) -> Dict[str, float]:
    """Return error metrics for key Calc columns."""
    raise NotImplementedError("Implement Calc comparison.")
