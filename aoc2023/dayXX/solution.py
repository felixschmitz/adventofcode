import aoc_helper
from pathlib import Path


def first_task(path: str):
    raw = aoc_helper.load_data(path)
    return None


def second_task(path: str):
    raw = aoc_helper.load_data(path)
    return None


if __name__ == "__main__":
    path = Path(__file__).parent / "input.txt"

    print("---Part One---")
    print(first_task(path))

    print("---Part Two---")
    print(second_task(path))
