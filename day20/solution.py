from collections import deque

def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read().splitlines()


def solve(content, pt2 = False) -> int:
    content = deque([*map(lambda n: int(n) * (811589153 if pt2 else 1), content)])
    indexes = deque(range(0, (length := len(content))))

    current_value = 0
    for _ in range(10 if pt2 else 1):
        for idx in range(length):
            position = indexes.index(idx)
            for deq in [content, indexes]:
                deq.rotate(position * -1)
                local_value = deq.popleft()
                if deq == content: current_value = local_value
                deq.rotate(current_value * -1)
                deq.appendleft(local_value)

    zero = content.index(0)
    a, b, c = (content[(zero + 1000) % (len(content))],
               content[(zero + 2000) % (len(content))],
               content[(zero + 3000) % (len(content))])
    return sum([a,b,c])
        

def first_task(file: str) -> int:
    content = load_data(file)
    ans = solve(content)
    return ans


def second_task(file: str) -> int:
    content = load_data(file)
    ans = solve(content, True)
    return ans

ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
