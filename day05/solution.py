def load_data(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as fhandle:
        return fhandle.read()


def parse_content(content: str) -> tuple:
    blocks = [[line for line in block.splitlines()] for block in content.split('\n\n')]
    stacks = [[e for idx, e in enumerate(list(elem)) if idx % 4 == 1] for elem in blocks[0]]
    stacks = [[subl[idx] for subl in stacks[:-1] if subl[idx] != ' '] for idx, value in enumerate(stacks[-1])]
    instructions = [[int(i) for i in instruction.split(' ') if i.isdigit()] for instruction in blocks[1]]
    return stacks, instructions


def perform_instructions(stacks: list, instructions: list, task: int) -> list:
    for idx, instr in enumerate(instructions):
        stack_movement = [stacks[(instr[1] - 1)].pop(0) for idx in range(instr[0])]
        if task == 1:
            stacks[instr[2] - 1] = list(reversed(stack_movement)) + stacks[instr[2] - 1]
        else: 
            stacks[instr[2] - 1] = stack_movement + stacks[instr[2] - 1]
    return stacks


def first_task(file: str) -> int:
    content = load_data(file)
    stacks, instructions = parse_content(content)
    final_stacks = perform_instructions(stacks, instructions, 1)
    return ''.join([stack[0] for stack in final_stacks])


def second_task(file: str) -> int:
    content = load_data(file)
    stacks, instructions = parse_content(content)
    final_stacks = perform_instructions(stacks, instructions, 2)
    return ''.join([stack[0] for stack in final_stacks])


final_top = first_task('input.txt')
print('First task:', final_top)


final_top = second_task('input.txt')
print('First task:', final_top)
