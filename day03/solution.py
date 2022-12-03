import string


def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()

    
def parse_data(content: str, task: int) -> list:
    rucksacks = [parse_rucksack(rucksack, task) for rucksack in content.splitlines()]
    if task == 2:
        rucksacks = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    return rucksacks


def parse_rucksack(rucksack: str, task: int) -> list:
    rucksack = [ord(supply) - 96 if supply.islower() else ord(supply) - 38 for supply in rucksack]
    if task == 1:
        rucksack = [rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
    return rucksack


def compartment_intersection(rucksack: list) -> int:
    intersection = set(rucksack[0]).intersection(rucksack[1])
    for elem in intersection:
        break
    return elem


def group_intersection(group: list) -> int:
    intersection = set(group[0]).intersection(group[1], group[2])
    for elem in intersection:
        break
    return elem


def first_task(file: str) -> int:
    content = load_data(file)
    rucksacks = parse_data(content, 1)
    priorities_sum = 0
    for rucksack in rucksacks:
        priorities_sum += compartment_intersection(rucksack)
    return priorities_sum


def second_task(file: str) -> int:
    content = load_data(file)
    rucksacks = parse_data(content, 2)
    priorities_sum = 0
    for group in rucksacks:
        priorities_sum += group_intersection(group)
    return priorities_sum


priorities_sum = first_task('input.txt')
print('First task:', priorities_sum)

priorities_sum = second_task('input.txt')
print('Second task:', priorities_sum)
