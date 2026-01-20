"""Measures sheet aggregation."""

from typing import Dict

import pandas as pd


def summarize_measures(calc_df: pd.DataFrame) -> Dict[str, float]:
    """Aggregate Calc outputs into Measures totals."""
    raise NotImplementedError("Implement Measures aggregation.")
