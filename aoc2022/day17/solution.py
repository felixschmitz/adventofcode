from copy import deepcopy
from dataclasses import dataclass

from tqdm import trange


def load_data(file: str) -> list:
    jet_map = {'>': 'right', '<': 'left'}
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [jet_map[prompt] for prompt in fhandle.read()]


WIDTH = 7


@dataclass
class Shape:
    kind: int
    zs: set[complex]

    def lim(self, func, attr):
        return func(getattr(z, attr) for z in self.zs)

    def move(self, dz: complex) -> "Shape":
        if dz.real + self.lim(min, "real") < 0:
            return self
        if dz.real + self.lim(max, "real") >= WIDTH:
            return self

        self.zs = {z + dz for z in self.zs}
        return self


SHAPES = [
    # h. line
    Shape(kind=1, zs={0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j}),
    # plus
    Shape(kind=2, zs={1 + 0j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 2j}),
    # inverse L
    Shape(kind=3, zs={0 + 0j, 1 + 0j, 2 + 0j, 2 + 1j, 2 + 2j}),
    # v. line
    Shape(kind=4, zs={0 + 0j, 0 + 1j, 0 + 2j, 0 + 3j}),
    # square
    Shape(kind=5, zs={0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j}),
]


def simulate(wind: list[str], num_iter: int, use_cache=False) -> list[int]:
    occ = {x + 0j for x in range(WIDTH)}
    tops = [0]
    mem = {}
    s_idx = w_idx = 0

    for t in trange(num_iter):

        if use_cache:
            if (s_idx, w_idx) in mem:
                t_, top_ = mem[(s_idx, w_idx)]
                tau = t - t_
                dH = tops[-1] - top_
                d, m = divmod(num_iter - t_, tau)
                if m == 0:
                    return t, int(top_ + d * dH)
            else:
                mem[(s_idx, w_idx)] = (t, tops[-1])

        # spawn a new shape
        shape = deepcopy(SHAPES[s_idx]).move(2 + (tops[-1] + 4) * 1j)
        s_idx = (s_idx + 1) % len(SHAPES)
        assert occ & shape.zs == set()

        while not (occ & shape.zs):
            w = wind[w_idx]
            w_idx = (w_idx + 1) % len(wind)
            if w == 'right':
                shape.move(1 + 0j)
                if shape.zs & occ:
                    shape.move(-1 + 0j)
            elif w == 'left':
                shape.move(-1 + 0j)
                if shape.zs & occ:
                    shape.move(1 + 0j)
            else:
                assert False

            shape.move(0 - 1j)
        shape.move(0 + 1j)  # final position
        occ |= shape.zs
        tops.append(int(max(z.imag for z in occ)))

    return tops


def first_task(file: str, num_iter: int) -> int:
    content = load_data(file)
    ans = simulate(content, num_iter, use_cache=False)[-1]
    return ans


def second_task(file: str, num_iter: float) -> int:
    content = load_data(file)
    ans = simulate(content, int(num_iter), use_cache=True)[-1]
    return ans

ans = first_task('input.txt', 2022)
print('First task:', ans)

ans = second_task('input.txt', 1e12)
print('Second task:', ans)
