"""Excel file IO helpers using named ranges."""

import json
import re
from pathlib import Path
from typing import Dict, Any, Optional, Union

import pandas as pd
import numpy as np


class ExcelReader:
    """Helper class to read values from Excel using named ranges."""

    def __init__(self, excel_path: Path, named_ranges_path: Optional[Path] = None):
        self.excel_path = excel_path
        if named_ranges_path is None:
            named_ranges_path = Path(__file__).parent.parent / "config" / "named_ranges.json"

        with open(named_ranges_path, "r") as f:
            self.named_ranges = json.load(f)

        self._sheets: Dict[str, pd.DataFrame] = {}

    def _get_sheet(self, sheet_name: str) -> pd.DataFrame:
        """Cache and return a sheet as a DataFrame."""
        if sheet_name not in self._sheets:
            # We read without header to use absolute indexing from named ranges
            self._sheets[sheet_name] = pd.read_excel(
                self.excel_path, sheet_name=sheet_name, header=None, engine="openpyxl"
            )
        return self._sheets[sheet_name]

    def get_value(self, name: str, default: Any = None) -> Any:
        """Get a single value by named range."""
        if name not in self.named_ranges:
            return default

        address = self.named_ranges[name]
        # Parse address like "Assumption!$E$25" or "'Other Input'!$D$21"
        match = re.match(r"['\"]?([^!]+)['\"]?!\$([A-Z]+)\$(\d+)", address)
        if not match:
            # Try range match like "Measures!$G$56:$G$57"
            return default

        sheet_name, col_str, row_str = match.groups()
        sheet_name = sheet_name.strip("'\"")

        # Convert Excel column (A, B, C...) to 0-indexed integer
        col_idx = 0
        for char in col_str:
            col_idx = col_idx * 26 + (ord(char) - ord('A') + 1)
        col_idx -= 1

        # print(f"DEBUG: {name} -> {sheet_name} {col_str}({col_idx}) {row_str}")

        # Convert Excel row (1-indexed) to 0-indexed
        row_idx = int(row_str) - 1

        try:
            df = self._get_sheet(sheet_name)
            val = df.iloc[row_idx, col_idx]
            if pd.isna(val):
                return default
            return val
        except Exception:
            return default

    def get_df(self, sheet_name: str, **kwargs) -> pd.DataFrame:
        """Read a whole sheet as a DataFrame."""
        return pd.read_excel(self.excel_path, sheet_name=sheet_name, engine="openpyxl", **kwargs)
