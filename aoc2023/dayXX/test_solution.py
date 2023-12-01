from pathlib import Path
from solution import first_task, second_task


def test_first_task():
    sample_path = Path(__file__).parent / "sample_input.txt"
    first_task(sample_path)
    assert True == True


def test_task2():
    sample_path = Path(__file__).parent / "sample_input.txt"
    second_task(sample_path)
    assert True == True
