from solution import first_task, second_task

def test_first_task():
    points = first_task('sample_input.txt')
    assert points == 15


def test_task2():
    points = second_task('sample_input.txt')
    assert points == 12
    