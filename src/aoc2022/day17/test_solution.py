from solution import first_task, second_task

def test_first_task():
    ans = first_task('sample_input.txt', 2022)
    assert type(ans) == int
    assert ans == 3068


def test_second_task():
    ans = second_task('sample_input.txt', 1e12)
    assert type(ans) == int
    assert ans == 1514285714288
