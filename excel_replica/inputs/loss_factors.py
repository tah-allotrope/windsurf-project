"""Load PV/BESS degradation factors from Loss sheet."""

from typing import Dict, List

import pandas as pd


def load_loss_factors(df: pd.DataFrame) -> Dict[str, List[float]]:
    """Return PV/BESS degradation arrays."""
    raise NotImplementedError("Implement Loss factor parsing.")
