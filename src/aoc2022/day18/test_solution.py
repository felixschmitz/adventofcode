from solution import first_task, second_task


def test_first_task():
    ans = first_task('sample_input.txt', 30)
    assert type(ans) == int
    assert ans == 64


def test_second_task():
    ans = second_task('sample_input.txt', 26)
    assert type(ans) == int
    assert ans == 58
