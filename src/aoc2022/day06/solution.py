def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()


def find_marker(content: str) -> int:
    for i, value in enumerate(content):
        if len(set(content[i - 4 : i])) == 4:
            return i


def find_message(content: str) -> int:
    for i, value in enumerate(content):
        if len(set(content[i - 14 : i])) == 14:
            return i


def first_task(file: str) -> int:
    content = load_data(file)
    marker_index = find_marker(content)
    return marker_index


def second_task(file: str) -> int:
    content = load_data(file)
    message_index = find_message(content)
    return message_index


marker_index = first_task('input.txt')
print('First task:', marker_index)


message_index = second_task('input.txt')
print('First task:', message_index)
