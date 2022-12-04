def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()


def iteratively_count(content: str, task: int) -> int:
    count = 0
    for line in content.splitlines():
        line = line.replace('-', ',').split(',')
        pair = [int(value) for value in line]
        conditions = [
            [
                pair[0] <= pair[2] and pair[1] >= pair[3], 
                pair[2] <= pair[0] and pair[3] >= pair[1]], 
            [
                pair[2] <= pair[1] and pair[3] >= pair[0]]]
        for condition in conditions[task]:
            if condition:
                count += 1
                break
    return count


def first_task(file: str) -> int:
    content = load_data(file)
    count = iteratively_count(content, 0)
    return count


def second_task(file: str) -> int:
    content = load_data(file)
    count = iteratively_count(content, 1)
    return count


count = first_task('input.txt')
print('First task:', count)


count = second_task('input.txt')
print('Second task:', count)
