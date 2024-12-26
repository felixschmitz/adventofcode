from pathlib import Path
from .solution import first_task, second_task

SAMPLE_PATH = Path(__file__).parent / "sample_input.txt"


def test_first_task():
    solution = first_task(SAMPLE_PATH)
    assert solution == 142


def test_task2():
    solution = second_task(SAMPLE_PATH)
    assert solution == 281
