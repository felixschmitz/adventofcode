import ast
from itertools import zip_longest


def first_load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [[ast.literal_eval(line) for line in packet.splitlines()] for packet in fhandle.read().split('\n\n')]


def second_load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [ast.literal_eval(line) for line in fhandle.read().splitlines() if len(line) != 0]


def order_check(left: list, right: list) -> int:
    result = None
    while result == None:
        if type(left) != type(right):
            if isinstance(left, list):
                right = [right]
            else:
                left = [left]
        if isinstance(left, list):
            for l, r in zip_longest(left, right):
                if l == None:
                    return True
                elif r == None:
                    return False
                result = order_check(l, r)
                if result != None:
                    return result
        else:
            if left < right:
                return True
            elif left == right:
                return None
            else:
                return False
        return result


def first_task(file: str) -> int:
    content = first_load_data(file)
    sum_ = 0
    for idx, packet in enumerate(content):
        left, right = packet
        if order_check(left, right):
            sum_ += idx + 1
    return sum_


def second_task(file: str) -> int:
    content = second_load_data(file)
    ordered = []
    while len(content) > 0:
        s_line = content[0]
        s_idx = 0
        for idx, line in enumerate(content[1:]):
            if not order_check(s_line, line):
                s_line = line
                s_idx = idx + 1
        ordered.append(content.pop(s_idx))
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
