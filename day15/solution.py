import re

def parse_data(file: str) -> list:
    ints = lambda s: map(int, re.findall(r'-?\d+', s))
    return [(x, y, M_distance(x,y,p,q)) for x,y,p,q in map(ints, open(file))]


def M_distance(x: int, y: int, p: int, q: int) -> int:
    return abs(x-p) + abs(y-q)


def part_1(sensors: list, limit: int):
    return (max(x - abs(limit-y) + d for x,y,d in sensors) - min(x + abs(limit-y) - d for x,y,d in sensors))



def part_2(sensors: list, limit: int):
    for xa, ya, da in sensors:
        for xb, yb, db in sensors:
            a, b = xa-ya-da, xb+yb+db
            X, Y = (b+a)//2, (b-a)//2+1
            if 0<X<limit and 0<Y<=limit and all(M_distance(X,Y,x,y)>d for x,y,d in sensors):
                return 4_000_000*X + Y


def first_task(file: str, limit=4_000_000) -> int:
    sensors = parse_data(file)
    ans = part_1(sensors, limit // 2)
    return ans


def second_task(file: str, limit=4_000_000) -> int:
    sensors = parse_data(file)
    ans = part_2(sensors, limit)
    return ans


ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
