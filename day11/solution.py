def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [monkey for monkey in fhandle.read().split('\n\n')]


def parse_data(content: list) -> list:
    monkeys = []
    for monkey in content:
        values = {}
        for m in monkey.split('\n'):
            if 'Monkey' not in m and len(m) != 0:
                key, value = [i.strip() for i in m.split(':')]
                if key == 'Starting items':
                    value = [int(i.strip('')) for i in value.split(',')]
                values[key] = value
        monkeys.append(values)
    return monkeys


def worriless_play_rounds(monkeys: list) -> int:
    inspected_elements = [0] * len(monkeys)
    for round in range(20):
        for monkey_id, monkey in enumerate(monkeys):
            monkey = monkeys[monkey_id].copy()
            items = monkey['Starting items'].copy()
            shift = 0
            for idx, item in enumerate(items):
                idx += shift
                inspected_elements[monkey_id] += 1
                operation = monkey['Operation'].split('=')[1].replace('old', str(item))
                worry_level = int(eval(operation)) // 3
                test_value = int(monkey['Test'].rsplit(' ', 1)[1])
                if worry_level % test_value == 0:
                    X = int(monkey['If true'].rsplit(' ', 1)[1])
                    monkeys[X]['Starting items'].append(worry_level)
                    shift -= 1
                else:
                    Y = int(monkey['If false'].rsplit(' ', 1)[1])
                    monkeys[Y]['Starting items'].append(worry_level)
                    shift -= 1
            monkeys[monkey_id]['Starting items'] = []
    l = list(sorted(inspected_elements))[-2:]
    return l[0] * l[-1]


def worried_play_rounds(monkeys: list) -> int:
    inspected_elements = [0] * len(monkeys)
    for round in range(10000):
        for monkey_id, monkey in enumerate(monkeys):
            monkey = monkeys[monkey_id].copy()
            items = monkey['Starting items'].copy()
            shift = 0
            for idx, item in enumerate(items):
                idx += shift
                inspected_elements[monkey_id] += 1
                operation = monkey['Operation'].split('=')[1].replace('old', str(item))
                worry_level = int(eval(operation))
                test_value = int(monkey['Test'].rsplit(' ', 1)[1])
                if worry_level % test_value == 0:
                    X = int(monkey['If true'].rsplit(' ', 1)[1])
                    monkeys[X]['Starting items'].append(worry_level)
                    shift -= 1
                else:
                    Y = int(monkey['If false'].rsplit(' ', 1)[1])
                    monkeys[Y]['Starting items'].append(worry_level)
                    shift -= 1
            monkeys[monkey_id]['Starting items'] = []
    l = list(sorted(inspected_elements))[-2:]
    print(l)
    return l[0] * l[-1]


def first_task(file: str) -> int:
    content = load_data(file)
    monkeys = parse_data(content)
    prod_ = worriless_play_rounds(monkeys)
    return prod_


def second_task(file: str) -> int:
    content = load_data(file)
    monkeys = parse_data(content)
    prod_ = worried_play_rounds(monkeys)
    return prod_


prod_ = first_task('input.txt')
print('First task:', prod_)

prod_ = second_task('input.txt')
print('Second task:', prod_)
