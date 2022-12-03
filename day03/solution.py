import string


def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()

    
def parse_data(content: str) -> list:
    rucksacks = [parse_rucksack(rucksack) for rucksack in content.splitlines()]
    return rucksacks


def parse_rucksack(rucksack: str) -> list:
    rucksack = [ord(supply) - 96 if supply.islower() else ord(supply) - 38 for supply in rucksack]
    rucksack = [rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
    return rucksack


def compartment_intersection(rucksack: list) -> int:
    intersection = set(rucksack[0]).intersection(rucksack[1])
    for elem in intersection:
        break
    return elem



def first_task(file: str) -> int:
    content = load_data(file)
    rucksacks = parse_data(content)
    priorities_sum = 0
    for rucksack in rucksacks:
        priorities_sum += compartment_intersection(rucksack)
    return priorities_sum


priorities_sum = first_task('input.txt')
print('First task:', priorities_sum)
