from solution import first_task, second_task

def test_first_task():
    ans = first_task('sample_input.txt')
    assert type(ans) == int
    assert ans == 152


def test_second_task():
    ans = second_task('sample_input.txt')
    assert type(ans) == int
    assert ans == 301
