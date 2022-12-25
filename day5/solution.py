import re
from copy import deepcopy


def parse(file_name):
    with open(file_name, "r") as file:
        stacks, instructions = file.read().split("\n\n")
        
    stacks = stacks.splitlines()
    stacks = {
        i+1: [
            stacks[-2-j][1+i*4]
            for j in range(len(stacks) - 1)
            if stacks[-2-j][1+i*4].isalpha()
        ]
        for i in range(len(stacks[-1].split()))
    }

    pattern = re.compile("move (\d+) from (\d+) to (\d+)")
    instructions = [
        list(map(int, match.groups()))
        for match in re.finditer(pattern, instructions)
    ]

    return stacks, instructions

def part1(data):
    stacks = deepcopy(data[0])
    for move, from_i, to_i in data[1]:
        stacks[to_i] += stacks[from_i][-move:][::-1]
        stacks[from_i] = stacks[from_i][:-move]
    return "".join([stacks[i+1][-1] for i in range(len(stacks))])

def part2(data):
    stacks = deepcopy(data[0])
    for move, from_i, to_i in data[1]:
        stacks[to_i] += stacks[from_i][-move:]
        stacks[from_i] = stacks[from_i][:-move]
    return "".join([stacks[i+1][-1] for i in range(len(stacks))])
