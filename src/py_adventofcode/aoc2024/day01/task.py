import numpy as np
import pytask
from pytask import task
from pathlib import Path
from typing import Annotated

from adventofcode.config import DATASET_NAMES, INPUTS2024, OUTPUTS2024
from adventofcode.utilities import read_input, format_output

def _calculate_total_abs_distance(data: np.ndarray) -> int:
    sorted_data = np.sort(data, axis=0)
    abs_differences = np.abs(np.diff(sorted_data, axis=1))
    return np.sum(abs_differences)

def _calculate_similarity_score(data: np.ndarray) -> int:
    sum_ = 0
    right_values, right_count = np.unique(data[:, 1], return_counts=True)
    left_values, left_count = np.unique(data[:, 0], return_counts=True)
    for left_value, left_count in zip(left_values, left_count):
        if left_value in right_values:
            index = np.where(right_values == left_value)[0][0]
            sum_ += left_value * left_count * right_count[index]
    return sum_


for dataset_name in ["sample", "inputs"]:

    @task(id=dataset_name)
    def solve_part_1(
        path_to_data: Annotated[Path, INPUTS2024 / "day01" / f"{dataset_name}.txt"],
        dataset_name: str=dataset_name,
    ) -> Annotated[Path, OUTPUTS2024 / "day01" / f"{dataset_name}_part_1.txt"]:
        location_ids = read_input(path_to_data)
        total_abs_distance = _calculate_total_abs_distance(location_ids)
        return format_output(total_abs_distance)

    @task(id=dataset_name)
    def solve_part_2(
        path_to_data: Annotated[Path, INPUTS2024 / "day01" / f"{dataset_name}.txt"],
        dataset_name: str=dataset_name,
    ) -> Annotated[Path, OUTPUTS2024 / "day01" / f"{dataset_name}_part_2.txt"]:
        location_ids = read_input(path_to_data)
        similarity_score = _calculate_similarity_score(location_ids)
        return format_output(similarity_score)