def data_loader(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def data_parser(content: str) -> list:
    return list(map(int, content.splitlines()))


def depth_transformer(data: list) -> list:
    return [data[i] - data[i - 1] > 0 for i in range(1, len(data))]


def sliding_window(data: list, window_size: int) -> list:
    return list(
        map(
            sum, [data[i : i + window_size] for i in range(len(data) - window_size + 1)]
        )
    )


def first_task(file: str):
    content = data_loader(file)
    data = data_parser(content)
    data_increasing = depth_transformer(data)
    return sum(data_increasing)


def second_task(file: str):
    content = data_loader(file)
    data = data_parser(content)
    data_windows = sliding_window(data, 3)
    data_increasing = depth_transformer(data_windows)
    return sum(data_increasing)


increase_counter = first_task("input.txt")
print("First task:", increase_counter)

increase_window_counter = second_task("input.txt")
print("Second task:", increase_window_counter)
