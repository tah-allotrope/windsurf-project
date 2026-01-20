"""Load and normalize the Data Input sheet."""

from dataclasses import dataclass
from typing import Optional

import pandas as pd


@dataclass
class DataInput:
    datetime: pd.Series
    solar_profile_kw: pd.Series
    load_kw: pd.Series


def load_data_input(df: pd.DataFrame) -> DataInput:
    """Extract the hourly solar and load profiles from the Data Input sheet."""
    raise NotImplementedError("Implement Data Input parsing.")
