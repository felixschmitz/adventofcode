from solution import first_task, second_task

def test_first_task():
    final_top = first_task('sample_input.txt')
    assert type(final_top) == str
    assert final_top == 'CMZ'


def test_second_task():
    final_top = second_task('sample_input.txt')
    assert type(final_top) == str
    assert final_top == 'MCD'