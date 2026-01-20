"""Excel file IO helpers."""

from typing import Dict

import pandas as pd


def read_excel_sheets(file_path: str, sheet_names: Dict[str, str]) -> Dict[str, pd.DataFrame]:
    """Load requested sheets from the Excel model."""
    raise NotImplementedError("Implement Excel reader.")
