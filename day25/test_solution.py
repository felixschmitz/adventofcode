from solution import first_task

def test_first_task():
    ans = first_task('sample_input.txt')
    assert type(ans) == str
    assert ans == '2=-1=0'
