from solution import first_task, second_task
import os

def test_first_task():
    result = [7, 5, 6, 10, 11]
    for file in os.listdir(os.getcwd()):
        if file.startswith('sample'):
            file_id = int(os.path.splitext(file)[0][-1])
            marker_index = first_task(file)
            assert type(marker_index) == int
            assert marker_index == result[file_id]


def test_second_task():
    result = [19, 23, 23, 29, 26]
    for file in os.listdir(os.getcwd()):
        if file.startswith('sample'):
            file_id = int(os.path.splitext(file)[0][-1])
            message_index = first_task(file)
            assert type(message_index) == int
            assert message_index == result[file_id]
