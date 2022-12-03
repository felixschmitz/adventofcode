from solution import first_task, second_task

def test_first_task():
    priorities_sum = first_task('sample_input.txt')
    assert priorities_sum == 157


def test_second_task():
    priorities_sum = second_task('sample_input.txt')
    assert priorities_sum == 70
    