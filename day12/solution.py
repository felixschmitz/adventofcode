from collections import deque


def load_data(file: str) -> list:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return [line for line in fhandle.read().splitlines()]


def find_start(content: list) -> tuple:
    return [(y_idx, y.index('S')) for y_idx, y in enumerate(content) if 'S' in y][0]


def find_end(content: list) -> tuple:
    return [(y_idx, y.index('E')) for y_idx, y in enumerate(content) if 'E' in y][0]

def find_path(content: list) -> int:
    steps = 0
    order = 'E' + ''.join(list(map(chr, range(122, 96, -1)))) + 'S'
    S = find_start(content)
    E = find_end(content)
    current_position = E
    #q = deque()
    while current_position != S and steps < 50:
        steps += 1
        x, y = current_position
        current_height = content[x][y]
        borders = [x >= 0, x + 1 < len(content), y >= 0, y + 1 < len(content[0])]
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        #last_pos = current_position
        possible_pos = current_position
        for border, neighbor in zip(borders, neighbors):
            #print(current_position, neighbor)
            if border:
                n_x, n_y = neighbor
                #print(content[n_x][n_y])
                print('neighbor position under observation', neighbor, border)
                print(content[n_x][n_y])
                if order.index(content[n_x][n_y]) - 1 == order.index(current_height):
                    # checking if the neighbor is one step smaller
                    possible_pos = n_x, n_y
                    #last_pos = current_position
                    current_position = possible_pos
                    #print('smaller', current_position, (n_x, n_y), possible_pos)
                    break
                elif order.index(content[n_x][n_y]) == order.index(current_height):
                    #print('equal', current_position, (n_x, n_y), possible_pos)
                    if last_pos != (n_x, n_y):
                        possible_pos = n_x, n_y
                        #print(current_position, (n_x, n_y), possible_pos)

        last_pos = current_position 
        current_position = possible_pos
        #q.append((d + 1, ))
        print('current position', current_position)

                    #print(neighbor, current_height, neighbors)



        '''clockwise_neighbors = []
        if x != 0:
            # checking if there is a square above
            #
            clockwise_neighbors.append([content[x - 1][y], (x - 1, y)])
        if x != len(content):
            # checking if there is a square to the right
            clockwise_neighbors.append([content[x][y + 1], (x, y + 1)])
        if x != len(content):
            # checking if there is a square below
            clockwise_neighbors.append([content[x + 1][y], (x + 1, y)])
        if x != 0:
            # checking if there is a square to the left
            clockwise_neighbors.append([content[x][y - 1], (x, y - 1)])

        print(clockwise_neighbors)
        print(order[order.index(current_height) + 1])
        #print(order[order.index(current_height) + 1] in clockwise_neighbors)
        
        if order[order.index(current_height) + 1] in [i[0] for i in clockwise_neighbors]:
            # checking if one elevation level lower is neighboring
            neighbor = order[order.index(current_height) + 1]
            print([i.index(neighbor) for i in clockwise_neighbors])
            print(clockwise_neighbors[neighbor])
            current_position = clockwise_neighbors[neighbor]
        else:
            neighbor = order[order.index(current_height)]
            print(clockwise_neighbors[neighbor])
            current_position = clockwise_neighbors[neighbor]'''
    return steps



def first_task(file: str) -> int:
    content = load_data(file)
    steps = find_path(content)
    return steps


def second_task(file: str) -> int:
    content = load_data(file)
    return None


steps = first_task('sample_input.txt')
print('First task:', steps)

ans = second_task('sample_input.txt')
print('Second task:', ans)
