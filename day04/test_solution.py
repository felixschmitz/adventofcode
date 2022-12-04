from solution import first_task, second_task

def test_first_task():
    count = first_task('sample_input.txt')
    assert type(count) == int
    assert count == 2


def test_second_task():
    count = second_task('sample_input.txt')
    assert type(count) == int
    assert count == 4