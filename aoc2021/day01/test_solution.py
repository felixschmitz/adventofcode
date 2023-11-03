from solution import first_task


def test_first_task():
    increase_counter = first_task("sample_input.txt")
    assert increase_counter == 7
