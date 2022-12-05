from pathlib import Path
from copy import deepcopy


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = file.read().split("\n\n")
    stacks = [[row[i] for row in data[0].split("\n")[:-1][::-1] if row[i].isalpha()] for i in range(1, len(data[0].split("\n")[0]), 4)]
    instructions = [[int(x) - (1 if i != 1 else 0) for i, x in enumerate(row.split()) if x.isnumeric()] for row in data[1].split("\n")]
    return (stacks, instructions)

def part1(data):
    stacks = deepcopy(data[0])
    for move, from_i, to_i in data[1]:
        stacks[to_i] += stacks[from_i][-move:][::-1]
        stacks[from_i] = stacks[from_i][:-move]
    return "".join([stack[-1] for stack in stacks])

def part2(data):
    stacks = deepcopy(data[0])
    for move, from_i, to_i in data[1]:
        stacks[to_i] += stacks[from_i][-move:]
        stacks[from_i] = stacks[from_i][:-move]
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))