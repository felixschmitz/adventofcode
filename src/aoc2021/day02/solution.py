def data_loader(file: str) -> str:
    with open(file, "r", encoding="utf-8") as fhandle:
        return fhandle.read()


def movement_parser(content: str) -> tuple:
    horizontal_position = 0
    vertical_position = 0
    for line in content.splitlines():
        direction, value = line.split(" ")
        if direction == "forward":
            horizontal_position += int(value)
        elif direction == "up":
            vertical_position -= int(value)
        elif direction == "down":
            vertical_position += int(value)
    return horizontal_position, vertical_position


def aim_movement_parser(content: str) -> tuple:
    horizontal_position = 0
    vertical_position = 0
    aim_position = 0
    for line in content.splitlines():
        direction, value = line.split(" ")
        if direction == "forward":
            horizontal_position += int(value)
            vertical_position += int(value) * aim_position
        elif direction == "up":
            aim_position -= int(value)
        elif direction == "down":
            aim_position += int(value)
    return horizontal_position, vertical_position


def first_task(file: str):
    content = data_loader(file)
    horizontal, vertical = movement_parser(content)
    return horizontal * vertical


def second_task(file: str):
    content = data_loader(file)
    horizontal, vertical = aim_movement_parser(content)
    return horizontal * vertical


hv_product = first_task("input.txt")
print("First task:", hv_product)

hva_product = second_task("input.txt")
print("Second task:", hva_product)
