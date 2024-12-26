def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [list(map(int, line)) for line in fhandle.read().splitlines()]
    

def visibility_counter(grid: list) -> int:
    s = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            tree = grid[row][column]
            left_right_conditions = all(grid[row][x] < tree for x in range(column)) or all(grid[row][x] < tree for x in range(column + 1, len(grid[row])))
            top_bottom_conditions = all(grid[x][column] < tree for x in range(row)) or all(grid[x][column] < tree for x in range(row + 1, len(grid)))
            if left_right_conditions or top_bottom_conditions:
                s += 1
    return s


def visibile_area(grid: list) -> int:
    s = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            tree = grid[row][column]
            left = right = down = up = 0
            for x in range(column - 1, - 1, -1):
                left += 1
                if grid[row][x] >= tree:
                    break
            for x in range(column + 1, len(grid[row])):
                right += 1
                if grid[row][x] >= tree:
                    break
            for x in range(row - 1, -1, -1):
                up += 1
                if grid[x][column] >= tree:
                    break
            for x in range(row + 1, len(grid)):
                down += 1
                if grid[x][column] >= tree:
                    break
            s = max(s, left * right * down * up)
    return s


def first_task(file: str) -> int:
    grid = load_data(file)
    sum_ = visibility_counter(grid)
    return sum_


def second_task(file: str) -> int:
    grid = load_data(file)
    max_ = visibile_area(grid)
    return max_


sum_ = first_task('input.txt')
print('First task:', sum_)

max_ = second_task('input.txt')
print('Second task:', max_)
