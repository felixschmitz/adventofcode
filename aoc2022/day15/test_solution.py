from solution import first_task, second_task


def test_first_task():
    ans = first_task('sample_input.txt', 20)
    assert type(ans) == int
    assert ans == 26


def test_second_task():
    ans = second_task('sample_input.txt', 20)
    assert type(ans) == int
    assert ans == 56000011
