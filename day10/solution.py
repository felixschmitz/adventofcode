def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [line for line in fhandle.read().splitlines()]


def signal_processing(content: str) -> int:
    X = 1
    c = 0
    sum_ = 0
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    for line in content:
        for _ in range(2 if 'addx' in line else 1):
            c += 1
            if c in relevant_cycles:
                sum_ += X * c
        if 'addx' in line:
            X += int(line.rsplit(' ', 1)[1])
    return sum_


def sprite_drawing(content: str) -> list:
    X = 0
    c = 0
    CRT_output = []
    for line in content:
        for _ in range(2 if 'addx' in line else 1):
            row = c // 40
            if c % 40 == 0:
                CRT_output.append([])
            if X in [c - i - row * 40 for i in range(3)]:
                CRT_output[row].append('#')
            else:
                CRT_output[row].append('.')
            c += 1
        if 'addx' in line:
            X += int(line.rsplit(' ', 1)[1])
    return CRT_output
        

def first_task(file: str) -> int:
    content = load_data(file)
    sum_ = signal_processing(content)
    return sum_


def second_task(file: str) -> int:
    content = load_data(file)
    CRT_output = sprite_drawing(content)
    return CRT_output



ans = first_task('input.txt')
print('First task:', ans)

CRT_output = second_task('input.txt')
print('Second task:')
for line in CRT_output:
    print(line)