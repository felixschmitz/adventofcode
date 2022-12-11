from solution import first_task, second_task

def test_first_task():
    prod_ = first_task('sample_input.txt')
    assert type(prod_) == int
    assert prod_ == 10605


def test_second_task():
    prod_ = second_task('sample_input.txt')
    assert type(prod_) == int
    assert prod_ == 2713310158
