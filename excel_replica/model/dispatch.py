"""Dispatch logic and control flags."""

from typing import Dict

import pandas as pd


def apply_dispatch(calc_df: pd.DataFrame, assumptions: Dict[str, float]) -> pd.DataFrame:
    """Apply AllowDischarge, DischargeConditionFlag, and strategy mode rules."""
    raise NotImplementedError("Implement dispatch rules.")
