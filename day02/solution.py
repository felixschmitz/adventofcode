def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()

def parse_data(content: str) -> list:
    games = [tuple(game.replace(' ', '')) for game in content.splitlines()]
    return games

def myself_outcome(selection: tuple) -> tuple:
    loosing_combinations = [('A', 'Z'), ('C', 'Y'), ('B', 'X')]
    d = {'oponent': ['A', 'B', 'C'], 'myself': ['X', 'Y', 'Z']}
    selection_points_myself = d['myself'].index(selection[1]) + 1
    if d['oponent'].index(selection[0]) != d['myself'].index(selection[1]):
        if selection in loosing_combinations:
            return -1, selection_points_myself
        else:
            return 1, selection_points_myself
    else:
        return 0, selection_points_myself


def update_score(outcome: int, selection_points_myself: int) -> int:
    if outcome == 0:
        return 3 + selection_points_myself
    elif outcome == 1:
        return 6 + selection_points_myself
    else:
        return 0 + selection_points_myself


def first_task(file: str):
    content = load_data(file)
    games = parse_data(content)
    points_myself = 0
    for game in games:
        outcome, selection_points_myself = myself_outcome(game)
        points_myself += update_score(outcome, selection_points_myself)
    return points_myself

points_myself = first_task('input.txt')
print('First task:', points_myself)