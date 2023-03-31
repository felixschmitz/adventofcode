'''
Failed to solve without taking a look at solution here: https://github.com/hyper-neutrino/advent-of-code/tree/main/2022
Mainly struggled with finding the optimal path in the first part.
Basically implemented method from second part in the beginning. This solution doesn't recognize a 'faster' path to S tho.
'''
from collections import deque


def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [list(line) for line in fhandle.read().strip().splitlines()]


def find_pos(content: list, letter: str) -> tuple:
    x, y = [(y_idx, y.index(letter)) for y_idx, y in enumerate(content) if letter in y][0]
    if letter == 'S':
        content[x][y] = 'a'
    if letter == 'E':
        content[x][y] = 'z'
    return (x, y)


def find_path(content: list) -> int:
    starting_position = find_pos(content, 'S')
    E = find_pos(content, 'E')
    q = deque()
    q.append((0, starting_position[0], starting_position[1]))
    vis = {(starting_position[0], starting_position[1])}

    while q:
        steps, x, y = q.popleft()
        for n_x, n_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if n_x < 0 or n_y < 0 or n_x >= len(content) or n_y >= len(content[0]):
                # checking if neighbor is on grid
                continue
            if (n_x, n_y) in vis:
                # checking if neighbor has been visited
                continue
            if ord(content[n_x][n_y]) - ord(content[x][y]) > 1:
                # checking if the height-difference is climable
                continue
            if n_x == E[0] and n_y == E[1]:
                # checking if neighbor is end
                return steps + 1   
            vis.add((n_x, n_y))
            q.append((steps + 1, n_x, n_y))


def find_fastest_path(content: list) -> int:
    E = find_pos(content, 'E')
    q = deque()
    q.append((0, E[0], E[1]))
    vis = {(E[0], E[1])}

    while q:
        steps, x, y = q.popleft()
        for n_x, n_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if n_x < 0 or n_y < 0 or n_x >= len(content) or n_y >= len(content[0]):
                # checking if neighbor is on grid
                continue
            if (n_x, n_y) in vis:
                # checking if neighbor has been visited
                continue
            if ord(content[n_x][n_y]) - ord(content[x][y]) < -1:
                # checking if the height-difference is climable (backwards)
                continue
            if content[n_x][n_y] == 'a':
                # checking if neighbor is a
                return steps + 1   
            vis.add((n_x, n_y))
            q.append((steps + 1, n_x, n_y))
    

def first_task(file: str) -> int:
    content = load_data(file)
    steps = find_path(content)
    return steps


def second_task(file: str) -> int:
    content = load_data(file)
    steps = find_fastest_path(content)
    return steps


steps = first_task('input.txt')
print('First task:', steps)

ans = second_task('input.txt')
print('Second task:', ans)
