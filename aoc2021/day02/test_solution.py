from solution import first_task


def test_first_task():
    increase_window_counter = first_task("sample_input.txt")
    assert increase_window_counter == 5
