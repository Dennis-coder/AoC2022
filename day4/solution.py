from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [[[int(row) for row in elf.split("-")] for elf in pair.split(",")] for pair in file.read().split("\n")]
    return data

def part1(data):
    amount = 0
    for elf1, elf2 in data:
        if elf1[0] <= elf2[0] <= elf2[1] <= elf1[1] \
        or elf2[0] <= elf1[0] <= elf1[1] <= elf2[1]:
            amount += 1
    return amount


def part2(data):
    amount = 0
    for elf1, elf2 in data:
        if elf1[0] <= elf2[0] <= elf1[1] \
        or elf2[0] <= elf1[0] <= elf2[1]:
            amount += 1
    return amount


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))