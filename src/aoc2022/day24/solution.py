import math

def load_data(file: str) -> list[list]:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [line for line in fhandle.read().splitlines()]


def parse_data(data: list[list]) -> tuple:
    start = data[0].index('.')
    finish = data[-1].index('.')
    grid = [line[1:-1] for line in data[1:-1]]
    return grid, (start - 1, - 1), (finish - 1, len(grid))


def find_spots(grid: list[list], start: tuple, finish: tuple) -> list[set]:
    period = math.lcm(len(grid[0]), len(grid))
    winds = []
    directions = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
    all_cells = {(x, y) for x in range(len(grid[0])) for y in range(len(grid))} | {start, finish}
    safe_cells = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in '<>^v':
                winds.append([(x, y), directions[cell]])

    for _ in range(period):
        wind_cells = {pos for pos, _ in winds}
        safe_cells.append(all_cells - wind_cells)
        for wind in winds:
            x, y = wind[0]
            dx, dy = wind[1]
            wind[0] = ((x + dx) % len(grid[0]), (y + dy) % len(grid))

    return safe_cells


def move_course(safe_cells: list[set], start: tuple, finish: tuple, t):
    period = len(safe_cells)
    possible_cells = {start}
    while True:
        t += 1
        targets = set()
        for x, y in possible_cells:
            destinations = {(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
            safe_destinations = destinations & safe_cells[t % period]
            if finish in safe_destinations:
                return t
            targets |= safe_destinations
        possible_cells = targets



def first_task(file: str) -> int:
    data = load_data(file)
    grid, start, finish = parse_data(data)
    safe_cells = find_spots(grid, start, finish)
    ans = move_course(safe_cells, start, finish, 0)
    return ans


def second_task(file: str) -> int:
    data = load_data(file)
    grid, start, finish = parse_data(data)
    safe_cells = find_spots(grid, start, finish)
    first_trip = move_course(safe_cells, start, finish, 0)
    second_trip = move_course(safe_cells, finish, start, first_trip)
    third_trip = move_course(safe_cells, start, finish, second_trip)
    return third_trip


ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
