"""Lifetime (multi-year) expansion logic."""

from dataclasses import dataclass
from typing import Dict, List

import pandas as pd


@dataclass
class LifetimeResults:
    yearly: pd.DataFrame
    totals: Dict[str, float]


def simulate_lifetime(calc_year1: pd.DataFrame, pv_degradation: List[float], bess_degradation: List[float]) -> LifetimeResults:
    """Apply degradation and augmentation schedules across project life."""
    raise NotImplementedError("Implement lifetime simulation.")
