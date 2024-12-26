class Elf:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.next_square = None
 
    def find_next_square(self, elf_set: set[tuple[int, int]], round: int):
        n = (self.x, self.y - 1)
        ne = (self.x + 1, self.y - 1)
        nw = (self.x - 1, self.y - 1)
        s = (self.x, self.y + 1)
        se = (self.x + 1, self.y + 1)
        sw = (self.x - 1, self.y + 1)
        e = (self.x + 1, self.y)
        w = (self.x - 1, self.y)
        if set([n, ne, nw, s, se, sw, e, w]).isdisjoint(elf_set):
            self.next_square = None
            return self.next_square
        options = []
        options.append(n if set([n, ne, nw]).isdisjoint(elf_set) else None)
        options.append(s if set([s, se, sw]).isdisjoint(elf_set) else None)
        options.append(w if set([w, nw, sw]).isdisjoint(elf_set) else None)
        options.append(e if set([e, ne, se]).isdisjoint(elf_set) else None)
        for i in range(4):
            if options[(i + round) % 4] is not None:
                self.next_square = options[(i + round) % 4]
                return self.next_square
        return self.next_square
 
    def move(self):
        self.x, self.y = self.next_square


def parse_data(file: str) -> list[Elf]:
     with open(file, 'r', encoding='utf-8') as fhandle:
        return [Elf(c_, r_) for r_, row in enumerate(fhandle.readlines()) for c_, v in enumerate(row) if v == '#']
   

def get_range(elves: list[Elf]):
    xmin = min(elf.x for elf in elves)
    xmax = max(elf.x for elf in elves)
    ymin = min(elf.y for elf in elves)
    ymax = max(elf.y for elf in elves)
    return xmin, xmax, ymin, ymax
 
def print_elves(elves: list[Elf]):
    xmin, xmax, ymin, ymax = get_range(elves)
    grid = [['.'] * (xmax - xmin + 1) for _ in range(ymax - ymin + 1)]
    for elf in elves:
        grid[elf.y - ymin][elf.x - xmin] = '#'
    for row in grid:
        print(''.join(row))
 
def run_simulation(elves: list[Elf], second: bool=False):
    round = 0
    while True:
        proposed_squares = set()
        conflicts = set()
        elf_set = set(map(lambda elf: (elf.x, elf.y), elves))
        for elf in elves:
            proposed_square = elf.find_next_square(elf_set, round)
            if proposed_square is not None:
                if proposed_square in proposed_squares:
                    conflicts.add(proposed_square)
                else:
                    proposed_squares.add(proposed_square)
        if round == 10 and not second:
            xmin, xmax, ymin, ymax = get_range(elves)
            #print_elves(elves)
            return (xmax - xmin + 1)*(ymax - ymin + 1) - len(elves)
        round += 1
        if len(proposed_squares) == 0:
            break
        for elf in elves:
            if elf.next_square and elf.next_square not in conflicts:
                elf.move()
            elf.next_square = None

    if second:
        #print_elves(elves)
        return round


def first_task(file: str) -> int:
    elves = parse_data(file)
    ans = run_simulation(elves)
    return ans


def second_task(file: str) -> int:
    elves = parse_data(file)
    ans = run_simulation(elves, True)
    return ans


ans = first_task('input.txt')
print('First taks:', ans)

ans = second_task('input.txt')
print('Second taks:', ans)
