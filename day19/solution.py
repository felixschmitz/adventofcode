import re

class V():
    def __init__(s, *a): s.a = tuple(a)
    def __iter__(s):   return iter(s.a)
    def __lt__(s, t):  return s.a < t.a
    def __add__(s, t): return V(*[a+b for a,b in zip(s,t)])
    def __sub__(s, t): return V(*[a-b for a,b in zip(s,t)])


def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.readlines()
        

def parse_data(line: str) -> list:
    i,a,b,c,d,e,f = map(int, re.findall(r'\d+',line))
    return (i, (V(0,0,0,a), V(0,0,0,1)), (V(0,0,0,b), V(0,0,1,0)),
               (V(0,0,d,c), V(0,1,0,0)), (V(0,f,0,e), V(1,0,0,0)))
    '''with open(file, 'r', encoding='utf-8') as fhandle:
        return [list(i) for i in map(blueprint, fhandle.readlines())]'''

def run(blueprint, t):
    todo = [(V(0,0,0,0), V(0,0,0,1))]
    for _ in range(t):
        todo_ = list()
        for have, make in todo:
            for cost, more in blueprint:
                if all(h >= c for h,c in zip(have, cost)):
                    todo_.append((have-cost+make, make+more))
            todo_.append((have+make, make))
        todo = sorted(todo_, key=lambda a:a[0]+a[1])[-2000:]
    return max(todo)[0].a[0]


def parse(line):
    i,a,b,c,d,e,f = map(int, re.findall(r'\d+',line))
    return (i, (V(0,0,0,a), V(0,0,0,1)), (V(0,0,0,b), V(0,0,1,0)),
               (V(0,0,d,c), V(0,1,0,0)), (V(0,f,0,e), V(1,0,0,0)))


def first_task(file: str) -> int:
    content = load_data(file)
    ans = 0
    for i, *blueprint in map(parse_data, content):
        ans += run(blueprint, 24) * i
    return ans


def second_task(file: str) -> int:
    content = load_data(file)
    ans = 1
    for i, *blueprint in map(parse_data, content):
        ans *= run(blueprint, 32) if i<4 else 1
    return ans

ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
