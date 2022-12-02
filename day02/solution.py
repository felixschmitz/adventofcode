def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()


def parse_data(content: str) -> list:
    games = [parse_game(game) for game in content.splitlines()]
    return games


def parse_game(game: str):
    choices = ['A', 'B', 'C', 'X', 'Y', 'Z']
    game = game.replace(' ', '')
    game = [choices.index(choice) % 3 + 1 for choice in game]
    return game
    

def update_score_first(game: list) -> int:
    loosing_combinations = [[1, 3], [3, 2], [2, 1]]
    if game in loosing_combinations:
        return game[1]
    elif game[0] == game[1]:
        return game[1] + 3
    else:
        return game[1] + 6

def update_score_second(game: list) -> int:
    combinations = [[1, 3], [3, 2], [2, 1]]
    if game[1] == 1:
        idx = [combination[0] for combination in combinations].index(game[0])
        choice = combinations[idx][1]
        return choice
    elif game[1] == 2:
        choice = game[0]
        return choice + 3
    else:
        idx = [combination[1] for combination in combinations].index(game[0])
        choice = combinations[idx][0]
        return choice + 6


def first_task(file: str) -> int:
    content = load_data(file)
    games = parse_data(content)
    score = 0
    for game in games:
        score += update_score_first(game)
    return score


def second_task(file: str) -> int:
    content = load_data(file)
    games = parse_data(content)
    score = 0
    for game in games:
        score += update_score_second(game)
    return score



points = first_task('input.txt')
print('First task:', points)


points = second_task('input.txt')
print('Second task:', points)
