from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt" 

def parse():
    with open(get_path(), "r") as file:
        data = [sum([int(x) for x in elf.split()]) for elf in file.read().split("\n\n")]
    return data

def part1(data):
    elf = max(data)
    return elf

def part2(data):
    elfs = sorted(data, reverse=True)
    return sum(elfs[:3])


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))