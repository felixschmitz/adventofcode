from pathlib import Path
from .solution import first_task, second_task


def test_first_task():
    sample_path = Path(__file__).parent / "sample_input.txt"
    solution = first_task(sample_path)
    assert solution == 142


def test_task2():
    sample_path = Path(__file__).parent / "sample_input_2.txt"
    solution = second_task(sample_path)
    assert solution == 281
