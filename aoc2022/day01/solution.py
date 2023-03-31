def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()

def parse_data(content: str) -> list:
    calories = [sum(map(int, elf.splitlines())) for elf in content.split('\n\n')]
    return calories

def first_task(file: str):
    content = load_data(file)
    calories = parse_data(content)
    return calories, max(calories)

def second_task(file: str):
    calories, max_calories = first_task(file)
    calories_sorted = sorted(calories, reverse=True)
    return calories_sorted[:3], sum(calories_sorted[:3])

calories, max_calories = first_task('input.txt')
print('First task:', max_calories)

top_three_calories, sum_top_three = second_task('input.txt')
print('Second task:', sum_top_three)
