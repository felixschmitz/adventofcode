from pathlib import Path
from .solution import first_task, second_task

SAMPLE_PATH = Path(__file__).parent / "sample_input.txt"


def test_first_task():
    first_task(SAMPLE_PATH)
    assert True == True


def test_task2():
    second_task(SAMPLE_PATH)
    assert True == True
