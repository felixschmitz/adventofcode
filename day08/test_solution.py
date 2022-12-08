from solution import first_task, second_task

def test_first_task():
    sum_ = first_task('sample_input.txt')
    assert type(sum_) == int
    assert sum_ == 21


def test_second_task():
    max_ = second_task('sample_input.txt')
    assert type(max_) == int
    assert max_ == 8