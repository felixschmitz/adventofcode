from pathlib import Path


def first_task(path: str):
    raw = load_data(path)
    return None


def second_task(path: str):
    raw = load_data(path)
    return None

def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()


if __name__ == "__main__":
    path = Path(__file__).parent / "input.txt"

    print("---Part One---")
    print(first_task(path))

    print("---Part Two---")
    print(second_task(path))
