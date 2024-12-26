from solution import first_task, second_task

def test_first_task():
    calories, max_calories = first_task('sample_input.txt')
    assert calories[0] == 6000
    assert len(calories) == 5
    assert max_calories == 24000
    assert calories[3] == max_calories 


def test_task2():
    top_three_calories, sum_top_three = second_task('test_input.txt')
    assert top_three_calories[0] == 24000
    assert len(top_three_calories) == 3
    assert sum_top_three == 45000
