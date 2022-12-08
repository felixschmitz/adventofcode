def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.read().splitlines()]

    
def create_tree(content: list) -> dict:
    cwd = root = {}
    stack = []
    for line in content:
        if line[0] == '$':
            if line[2] == 'c':
                dir = line[5:]
                if dir == '/':
                    cwd = root
                    dir = []
                elif dir == '..':
                    cwd = stack.pop()
                else:
                    if dir not in cwd:
                        cwd[dir] = {}
                    stack.append(cwd)
                    cwd = cwd[dir]
        else:
            value, name = line.split()
            if value == 'dir':
                if name not in cwd:
                    cwd[name] = {}
            else:
                cwd[name] = int(value)
    return root


def sum_dirs(root: dict) -> int:
    if type(root) == int:
        return root, 0
    size = 0
    ans = 0
    for child in root.values():
        size_, ans_ = sum_dirs(child)
        size += size_
        ans += ans_
    if size <= 100000:
        ans += size
    return size, ans


def dir_size(dir: dict) -> int:
    if type(dir) == int:
        return dir
    return sum(map(dir_size, dir.values()))


def min_del_dir(dir: dict, space_needed: int) -> int:
    ans = float('inf')
    if dir_size(dir) >= space_needed:
        ans = dir_size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        temp = min_del_dir(child, space_needed)
        ans = min(ans, temp)
    return ans


def first_task(file: str) -> int:
    content = load_data(file)
    root = create_tree(content)
    _, sum_ = sum_dirs(root)
    return sum_


def second_task(file: str) -> int:
    content = load_data(file)
    root = create_tree(content)
    space_needed = dir_size(root) - 40_000_000
    ans = min_del_dir(root, space_needed)
    return ans

sum_ = first_task('input.txt')
print('First task:', sum_)

ans = second_task('input.txt')
print('Second task:', ans)
