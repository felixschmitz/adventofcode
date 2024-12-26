from pathlib import Path
from .solution import first_task, second_task

SAMPLE_PATH = Path(__file__).parent / "sample_input.txt"


def test_first_task():
    constraint = {"red": 12, "green": 13, "blue": 14}
    solution = first_task(SAMPLE_PATH, constraint)
    assert solution == 8


def test_task2():
    second_task(SAMPLE_PATH)
    assert True == True
