import re


class Valve:
    def __init__(self, name: str, flow_rate: int, children: list):
        self.name = name
        self.flow_rate = flow_rate
        self.children = children


def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [line for line in fhandle.readlines()]


def parse_data(content: list) -> dict:
    valves = {}
    for line in content:
        c_letters = list(map(str, re.findall(r'\b[A-Z]{2}', line)))
        valve_name = c_letters[0]
        flow_rate = list(map(int, re.findall(r'-?\d+', line)))[0]
        children = c_letters[1:]
        valves[valve_name] = Valve(valve_name, flow_rate, children)
    return valves


def floid_warshall(valves: dict) -> dict:
    dists = {v: {s: 1e6 for s in valves} for v in valves}
    for v in valves:
        dists[v][v] = 0
        for s in valves[v].children:
            dists[v][s] = 1
    for k in valves:
        for i in valves:
            for j in valves:
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    return dists


def generate_open_options(pos: str, open_valves: list, time_left: int, flowing_valves: list, distances: list):
        for next in flowing_valves:
            if next not in open_valves and distances[pos][next] <= time_left:
                open_valves.append(next)
                yield from generate_open_options(
                    next, open_valves, time_left - distances[pos][next] - 1, flowing_valves, distances
                )
                open_valves.pop()
        yield open_valves.copy()
 

def get_order_score(open_order: list, time_remaining: int, valves: dict, distances: dict):
    now, ans = 'AA', 0
    for pos in open_order:
        time_remaining -= distances[now][pos] + 1
        ans += valves[pos].flow_rate * time_remaining
        now = pos
    return ans


def get_score_together(ways: list, valves: dict, distances: dict) -> int:
    best_scores = {}
    for order in ways:
        tup = tuple(sorted(order))
        score = get_order_score(order, 26, valves, distances)
        best_scores[tup] = max(best_scores.get(tup, 0), score)
    best_scores = list(best_scores.items())

    ans = 0
    for human_idx in range(len(best_scores)):
        for elephant_idx in range(human_idx + 1, len(best_scores)):
            human_opens, human_score = best_scores[human_idx]
            elephant_opens, elephant_score = best_scores[elephant_idx]

            if len(set(human_opens).intersection(elephant_opens)) == 0:
                ans = max(ans, human_score + elephant_score)
    return ans


def first_task(file: str, t: int) -> int:
    content = load_data(file)
    valves = parse_data(content)
    distances = floid_warshall(valves)
    flowing_valves = [v for v in valves if valves[v].flow_rate > 0]
    ans = max(get_order_score(o, t, valves, distances) for o in generate_open_options('AA', [], t, flowing_valves, distances))
    return ans


def second_task(file: str, t: int) -> int:
    content = load_data(file)
    valves = parse_data(content)
    distances = floid_warshall(valves)
    flowing_valves = [v for v in valves if valves[v].flow_rate > 0]
    ways = list(generate_open_options('AA', [], t, flowing_valves, distances))
    ans = get_score_together(ways, valves, distances)
    return ans


ans = first_task('input.txt', 30)
print('First task:', ans)


ans = second_task('input.txt', 26)
print('Second task:', ans)
