"""Load assumption parameters and named ranges."""

from dataclasses import dataclass
from typing import Dict, Optional

import pandas as pd


@dataclass
class AssumptionConfig:
    step_hours: float
    strategy_mode: int
    bess_capacity_kwh: float
    bess_power_kw: float
    bess_efficiency: float
    min_reserve_soc_kwh: float


def load_assumptions(df: pd.DataFrame, named_ranges: Dict[str, str]) -> AssumptionConfig:
    """Parse the Assumption sheet and named ranges into a config object."""
    raise NotImplementedError("Implement Assumption parsing.")
