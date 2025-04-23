from pathlib import Path
import numpy as np

def read_input(input_path: Path) -> np.ndarray:
    return np.loadtxt(fname=input_path, dtype=int)

def format_output(output: np.ndarray) -> str:
    return str(output)