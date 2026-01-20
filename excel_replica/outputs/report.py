"""Generate markdown audit reports."""

from typing import Dict


def build_report(summary: Dict[str, float]) -> str:
    """Build the audit report markdown text."""
    raise NotImplementedError("Implement report builder.")
