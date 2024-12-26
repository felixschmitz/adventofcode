from pathlib import Path


def first_task(path: str, constraint: dict):
    raw = load_data(path)
    parseddata = _transform_and_read_data(raw)
    inferreddata = _max_color_values(parseddata)
    possbile_games = _possible_games(inferreddata, constraint)
    return sum(possbile_games)


def second_task(path: str):
    raw = load_data(path)
    return None


def _transform_and_read_data(raw: str) -> list:
    lines = raw.splitlines()
    games = []
    for line in lines:
        game = {}

        gameID, sets = line.split(":")
        game["game"] = int(gameID.split(" ")[1])

        listofsets = sets.split(";")
        for i, set in enumerate(listofsets):
            setcolors = {"red": 0, "green": 0, "blue": 0}
            for subset in set.split(", "):
                value, color = subset.split(" ")
                setcolors[color] = int(value)
            game[f"set{i + 1}"] = setcolors
            print(game)
        games.append(game)
    return games


def _max_color_values(data) -> list:
    games = []
    for parsedgame in data:
        game = {}
        game["game"] = parsedgame["game"]
        maxvalues = {"red": 0, "green": 0, "blue": 0}
        for key in parsedgame.keys():
            if key != "game":
                for color in maxvalues:
                    if parsedgame[key][color] > maxvalues[color]:
                        maxvalues[color] = parsedgame[key][color]
        game = game | maxvalues
        games.append(game)
    return games


def _possible_games(data, constraint) -> list:
    possible_games = []
    for game in data:
        conditions = (
            game["red"] <= constraint["red"]
            and game["green"] <= constraint["green"]
            and game["blue"] <= constraint["blue"]
        )
        if conditions:
            # print(game)
            possible_games.append(game["game"])
    return possible_games


def load_data(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


if __name__ == "__main__":
    path = Path(__file__).parent / "input.txt"

    constraint = {"red": 12, "green": 13, "blue": 14}
    print("---Part One---")
    print(first_task(path, constraint))

    print("---Part Two---")
    print(second_task(path))
