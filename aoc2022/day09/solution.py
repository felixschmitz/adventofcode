def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.read().splitlines()]


def first_rope_movement(content: str) -> int:
    tail_trace = set()
    head_pos = (0, 0)
    tail_pos = (0, 0)
    for line in content:
        dir = line[0]
        for _ in range(1, int(line[2:]) + 1):
            head_pos = head_movement(dir, head_pos)
            tail_pos = tail_movement(head_pos, tail_pos)
            tail_trace.add(tail_pos)
    return len(tail_trace)


def second_rope_movement(content: str) -> int:
    tail_trace = set()
    S = [(0, 0) for _ in range(10)]
    for line in content:
        dir = line[0]
        for _ in range(1, int(line[2:]) + 1):
            S[0] = head_movement(dir, S[0])
            #print(S[0])
            for i in range(9):
                S[i + 1] = tail_movement(S[i], S[i + 1])
            tail_trace.add(S[-1]) 
    return len(tail_trace)


def head_movement(dir: str, head_pos: tuple) -> tuple:
    if dir == 'L':
        head_pos = head_pos[0], head_pos[1] - 1
    elif dir == 'R':
        head_pos = head_pos[0], head_pos[1] + 1
    elif dir == 'U':
        head_pos = head_pos[0] + 1, head_pos[1]
    else:
        head_pos = head_pos[0] - 1, head_pos[1]
    return head_pos


def tail_movement(head_pos: tuple, tail_pos: tuple) -> tuple:
    if abs(head_pos[0] - tail_pos[0]) + abs(head_pos[1] - tail_pos[1]) > 2:
        if head_pos[0] - tail_pos[0] > 0 and head_pos[1] - tail_pos[1] > 0:
            tail_pos = tail_pos[0] + 1, tail_pos[1] + 1
        elif head_pos[0] - tail_pos[0] > 0 and head_pos[1] - tail_pos[1] < 0:
            tail_pos = tail_pos[0] + 1, tail_pos[1] - 1
        elif head_pos[0] - tail_pos[0] < 0 and head_pos[1] - tail_pos[1] > 0:
            tail_pos = tail_pos[0] - 1, tail_pos[1] + 1
        else:
            tail_pos = tail_pos[0] - 1, tail_pos[1] - 1
    elif abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
        if head_pos[0] - tail_pos[0] > 1:
            tail_pos = tail_pos[0] + 1, tail_pos[1]
        elif head_pos[0] - tail_pos[0] < -1:
            tail_pos = tail_pos[0] - 1, tail_pos[1]
        elif head_pos[1] - tail_pos[1] > 1:
            tail_pos = tail_pos[0], tail_pos[1] + 1
        else:
            tail_pos = tail_pos[0], tail_pos[1] -1
    return tail_pos
    

def first_task(file:str):
    content = load_data(file)
    sum_ = first_rope_movement(content)
    return sum_


def second_task(file:str):
    content = load_data(file)
    sum_ = second_rope_movement(content)
    return sum_


sum_ = first_task('input.txt')
print('First task:', sum_)

sum_ = second_task('input.txt')
print('Second task:', sum_)
