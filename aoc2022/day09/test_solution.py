from solution import first_task, second_task

def test_first_task():
    sum_ = first_task('sample_input.txt')
    assert type(sum_) == int
    assert sum_ == 13


def test_second_task():
    sum_ = second_task('sample_input2.txt')
    assert type(sum_) == int
    assert sum_ == 36
