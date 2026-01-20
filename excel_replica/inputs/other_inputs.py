"""Load Other Input sheet parameters and flags."""

from typing import Dict

import pandas as pd


def load_other_inputs(df: pd.DataFrame) -> Dict[str, float]:
    """Extract optional parameters used by strategy/financial calculations."""
    raise NotImplementedError("Implement Other Input parsing.")
