"""All the general configuration of the project."""

from pathlib import Path

SRC = Path(__file__).parent.resolve()
BLD = SRC / ".." / ".." / "bld"
INPUTS2024 = BLD / "inputs" / "aoc2024"
OUTPUTS2024 = BLD / "outputs" / "aoc2024"

DATASET_NAMES = ["sample", "inputs"]


__all__ = [
    "BLD",
    "DATASET_NAMES",
    "INPUTS2024",
    "SRC",
    "OUTPUTS2024",
]