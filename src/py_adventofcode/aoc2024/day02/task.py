import numpy as np
import pytask
from pytask import task
from pathlib import Path
from typing import Annotated

from adventofcode.config import DATASET_NAMES, INPUTS2024, OUTPUTS2024
from adventofcode.utilities import read_input, format_output

def _calculate_number_of_save_reports(data: np.ndarray) -> int:
    breakpoint()
    for report in data:
    return 0


for dataset_name in ["sample", "inputs"]:

    @task(id=dataset_name)
    def solve_part_1(
        path_to_data: Annotated[Path, INPUTS2024 / "day02" / f"{dataset_name}.txt"],
        dataset_name: str=dataset_name,
    ) -> Annotated[Path, OUTPUTS2024 / "day02" / f"{dataset_name}_part_1.txt"]:
        reports = read_input(path_to_data)
        total_abs_distance = _calculate_number_of_save_reports(reports)
        return format_output(total_abs_distance)

    @task(id=dataset_name)
    def solve_part_2(
        path_to_data: Annotated[Path, INPUTS2024 / "day02" / f"{dataset_name}.txt"],
        dataset_name: str=dataset_name,
    ) -> Annotated[Path, OUTPUTS2024 / "day02" / f"{dataset_name}_part_2.txt"]:
        reports = read_input(path_to_data)
        similarity_score = _calculate_similarity_score(reports)
        return format_output(similarity_score)