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
    data[0] = data[0].split("\n")
    stacks = []
    for i in range(1, len(data[0][0]), 4):
        stacks.append([])
    for row in data[0][:-1][::-1]:
        for i in range(1, len(row), 4):
            if row[i] != " ":
                stacks[i // 4].append(row[i])
    data[0] = stacks
    data[1] = [[int(x) for x in row.split() if x.isnumeric()] for row in data[1].split("\n")]
    return data

def part1(data):
    stacks = deepcopy(data[0])
    for move, from_i, to_i in data[1]:
        for _ in range(move):
            stacks[to_i - 1].append(stacks[from_i - 1].pop())
    answer = ""
    for stack in stacks:
        answer += stack.pop()
    return answer

def part2(data):
    stacks = deepcopy(data[0])
    for move, from_i, to_i in data[1]:
        stacks[to_i - 1] += stacks[from_i - 1][-move:]
        stacks[from_i - 1] = stacks[from_i - 1][:-move]
    answer = ""
    for stack in stacks:
        answer += stack.pop()
    return answer


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))