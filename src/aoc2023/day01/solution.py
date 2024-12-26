from pathlib import Path
import re


def first_task(path: str):
    raw = _load_data(path)
    digits_per_line = ["".join(re.findall(r"\d", line)) for line in raw.splitlines()]
    two_digits_lines = [int(n[0] + n[-1]) for n in digits_per_line]
    return sum(two_digits_lines)


def second_task(path: str, mapping: dict):
    raw = _load_data(path)
    cleaned_data = [_replace_substring(line, mapping) for line in raw.splitlines()]
    digits_per_line = ["".join(re.findall(r"\d", line)) for line in cleaned_data]
    two_digits_lines = [int(n[0] + n[-1]) for n in digits_per_line]
    return sum(two_digits_lines)


def _load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def _replace_substring(input_string, replacement_dict):
    for k, v in replacement_dict.items():
        input_string = input_string.replace(k, v)
    return input_string


if __name__ == "__main__":
    path = Path(__file__).parent / "input.txt"

    print("---Part One---")
    print(first_task(path))

    print("---Part Two---")
    mapping = {
        "zero": "zero0zero",
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }
    print(second_task(path, mapping))
