"""Compare Measures totals against Excel truth."""

from typing import Dict


def compare_measures(model_totals: Dict[str, float], excel_totals: Dict[str, float]) -> Dict[str, float]:
    """Return percent error for Measures totals."""
    raise NotImplementedError("Implement Measures comparison.")
