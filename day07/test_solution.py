from solution import first_task, second_task

def test_first_task():
    sum_ = first_task('sample_input.txt')
    assert type(sum_) == int
    assert sum_ == 95437


def test_second_task():
    ans = second_task('sample_input.txt')
    assert type(ans) == int
    assert ans == 24933642