from solution import first_task, second_task


def test_first_task():
    increase_counter = first_task("sample_input.txt")
    assert increase_counter == 7


def test_second_task():
    increase_window_counter = second_task("sample_input.txt")
    assert increase_window_counter == 5
