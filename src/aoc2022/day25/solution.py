def load_data(file: str) -> list[list]:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [[int(place.replace('-', '-1').replace('=', '-2')) for place in line] for line in fhandle.read().splitlines()]


def SNAFU_parse(data: list[list]) -> int:
    # Takes list of lists of SNAFU numbers as input and returns their decimal number sum
    l = []
    for line in data:
        base_five = [pow(5, i) for i in range(len(line))]
        l.append(sum([x * y for x, y in zip(base_five, reversed(line))]))
    return sum(l)


def decimal_parse(dec: int):
    # Takes decimal integer as input and returns respective SNAFU string
    if not dec:
        return ''
    q, r = divmod(dec + 2, 5)
    return decimal_parse(q) + '=-012'[r]


def first_task(file: str) -> int:
    data = load_data(file)
    digits = SNAFU_parse(data)
    ans = decimal_parse(digits)
    return ans


ans = first_task('input.txt')
print('First task:', ans)
