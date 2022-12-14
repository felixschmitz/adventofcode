def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [line for line in fhandle.read().splitlines()]


def parse_data(content: list) -> tuple:
    l = [[[int(coord) for coord in pos.strip().split(',')] for pos in path.split('->')] for path in content]
    min_ = [min([pos[0] for path in l for pos in path]), 0]
    sand_source = [m - n for m, n in zip([500, 0], min_)]
    return [[[m - n for m, n in zip(pos, min_)] for pos in path] for path in l], sand_source


def place_rocks(content: list, sand_source: list) -> int:
    num_r = max([pos[1] for path in content for pos in path]) + 1
    grid = [['.'] * num_r for _ in range(num_r)]
    grid[sand_source[1]][sand_source[0]] = '+'
    for path in content:
        for idx, step in enumerate(path):
            if idx < len(path) - 1:
                if path[idx][0] == path[idx + 1][0]:
                    # drawing vertical line
                    c = step[0]
                    row = step[1]
                    if path[idx + 1][1] - path[idx][1] > 0:
                        stride = 1
                        add_ = 1
                    else:
                         stride = -1
                         add_ = -1
                    for r in range(0, path[idx + 1][1] - path[idx][1] + add_, stride):
                        grid[row + r][c] = '#'
                elif path[idx][1] == path[idx + 1][1]:
                    # drawing horizontal line
                    column = step[0]
                    r = step[1]
                    if path[idx + 1][0] - path[idx][0] > 0:
                        stride = 1
                        add_ = 1
                    else:
                         stride = -1
                         add_ = -1
                    for c in range(0, path[idx + 1][0] - path[idx][0] + add_, stride):
                        grid[r][column + c] = '#'
    return grid


def pour_sand(grid: list, sand_source: list) -> int:
    steps = 0
    inside_grid = True
    while True:
        s_c, s_r = sand_source
        while inside_grid:
            try:
                if grid[s_r + 1][s_c] == '.':
                    s_c, s_r = s_c, s_r + 1
                else:
                    if grid[s_r + 1][s_c - 1] == '.':
                        s_c, s_r = s_c - 1, s_r + 1
                    elif grid[s_r + 1][s_c + 1] == '.':
                        s_c, s_r = s_c + 1, s_r + 1
                    else:
                        grid[s_r][s_c] = 'o'
                        break
            except IndexError:
                inside_grid = False
        if inside_grid == False:
            return steps
        steps += 1


def parse_data_floor(content: list) -> tuple:
    l = [[[int(coord) for coord in pos.strip().split(',')] for pos in path.split('->')] for path in content]
    min_ = min([pos[0] for path in l for pos in path])
    max_ = max([pos[0] for path in l for pos in path])
    span = max_ + min_
    sand_source = [500, 0]
    return [[[pos[0], pos[1]] for pos in path] for path in l], sand_source, span


def place_rocks_floor(content: list, sand_source: list, span: int) -> int:
    num_r = max([pos[1] for path in content for pos in path]) + 1
    grid = [['.'] * (num_r + 2 * span) for _ in range(num_r + 2)]
    grid[-1] = ['#'] * (num_r + 2 * span)
    grid[sand_source[1]][sand_source[0]] = '+'
    for path in content:
        for idx, step in enumerate(path):
            if idx < len(path) - 1:
                if path[idx][0] == path[idx + 1][0]:
                    c = step[0]
                    row = step[1]
                    if path[idx + 1][1] - path[idx][1] > 0:
                        stride = 1
                        add_ = 1
                    else:
                         stride = -1
                         add_ = -1
                    for r in range(0, path[idx + 1][1] - path[idx][1] + add_, stride):
                        grid[row + r][c] = '#'
                elif path[idx][1] == path[idx + 1][1]:
                    column = step[0]
                    r = step[1]
                    if path[idx + 1][0] - path[idx][0] > 0:
                        stride = 1
                        add_ = 1
                    else:
                         stride = -1
                         add_ = -1
                    for c in range(0, path[idx + 1][0] - path[idx][0] + add_, stride):
                        grid[r][column + c] = '#'
    return grid


def pour_sand_endlessly(grid: list, sand_source: list) -> int:
    steps = 0
    source_unblocked = True
    while True:
        s_c, s_r = sand_source
        while source_unblocked:
            if grid[s_r + 1][s_c] == '.':
                s_c, s_r = s_c, s_r + 1
            else:
                if grid[s_r + 1][s_c - 1] == '.':
                    s_c, s_r = s_c - 1, s_r + 1
                elif grid[s_r + 1][s_c + 1] == '.':
                    s_c, s_r = s_c + 1, s_r + 1
                else:
                    if [s_c, s_r] == sand_source:
                        source_unblocked = False
                    else:
                        grid[s_r][s_c] = 'o'
                    break
        steps += 1
        if source_unblocked == False:
            return steps
    

def first_task(file: str) -> int:
    content = load_data(file)
    parsed_content, sand_source = parse_data(content)
    grid = place_rocks(parsed_content, sand_source)
    ans = pour_sand(grid, sand_source)
    return ans


def second_task(file: str) -> int:
    content = load_data(file)
    parsed_content, sand_source, span = parse_data_floor(content)
    grid = place_rocks_floor(parsed_content, sand_source, span)
    ans = pour_sand_endlessly(grid, sand_source)
    return ans


ans = first_task('input.txt')
print('First task:', ans)

ans = second_task('input.txt')
print('Second task:', ans)
