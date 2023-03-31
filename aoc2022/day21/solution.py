def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [x.replace(':', '').split(' ') for x in fhandle.read().splitlines()]


def solve(data: list, second: bool=False) -> int:
    operations = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__floordiv__, '=': int.__eq__}
    monkeys = {}
    for monkey in data:
        if len(monkey) == 2:
            # lambda function for inherit value of monkey
            monkeys[monkey[0]] = lambda x=monkey[1]: int(x)
        else:
            # lambda function for value of monkey to be calculated
            monkeys[monkey[0]] = lambda x=monkey[1], y=monkey[2], z=monkey[3]: operations[y](monkeys[x](), monkeys[z]())
            if second and monkey[0] == 'root':
                a, b = monkey[1], monkey[3]
    if not second:
        # returning the value for the first task
        return monkeys['root']()

    start_x = monkeys[a]()
    start_y = monkeys[b]()
    start_value = monkeys['humn']()
    end_value = max([start_x, start_y]) ** 2
    monkeys['humn'] = lambda x=end_value: int(x)
    end_x = monkeys[a]()
    end_y = monkeys[b]()

    relevant_start, relevant_end = next(((x, y) for x, y in [(start_x, end_x), (start_y, end_y)] if x != y))

    static = next((x for x in [start_x, start_y] if x != relevant_start))

    diff_end_and_start_values = abs(end_value - start_value)
    diff_relevant_end_and_start = abs(relevant_end - relevant_start)
    diff_start_values = abs(relevant_start - static)

    steps_per_increase = diff_relevant_end_and_start / diff_end_and_start_values

    return round(diff_start_values / steps_per_increase) + start_value


def first_task(file: str) -> int:
    data = load_data(file)
    ans = solve(data)
    return ans


def second_task(file: str) -> int:
    data = load_data(file)
    ans = solve(data, True)
    return ans

ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
