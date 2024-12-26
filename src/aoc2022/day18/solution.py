import numpy as np
import fill_voids

def load_data(file: str) -> list:
    with open (file, 'r', encoding='utf-8') as fhandle:
        l = [[int(e) for e in line.split(',')] for line in fhandle.read().splitlines()]
        grid = np.zeros((max([c[0] for c in l]) + 2, max([c[1] for c in l]) + 2, max([c[2] for c in l]) + 2))
        for line in l:
            x, y, z = line
            grid[x][y][z] = 1
        return grid


def test_sides(x: int, y: int, z: int, grid: np.array) -> int:
    sides = 0

    if grid[x][y][z]:
        if not grid[x - 1][y][z]:
            sides += 1

        if not grid[x + 1][y][z]:
            sides += 1

        if not grid[x][y - 1][z]:
            sides += 1

        if not grid[x][y + 1][z]:
            sides += 1

        if not grid[x][y][z - 1]:
            sides += 1

        if not grid[x][y][z + 1]:
            sides += 1

    return sides


def untouched_sides(grid: np.array) -> int:
    s = 0
    for x in range(-1, grid.shape[0] - 1):
        for y in range(-1, grid.shape[1] - 1):
            for z in range(-1, grid.shape[2] - 1):
                s += test_sides(x, y, z, grid)
    return s


def first_task(file: str) -> int:
    grid = load_data(file)
    ans = untouched_sides(grid)
    return ans


def second_task(file: str) -> int:
    grid = load_data(file)
    fill_voids.fill(grid, in_place=True)
    ans = untouched_sides(grid)
    return ans


ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
