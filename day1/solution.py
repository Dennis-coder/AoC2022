from pathlib import Path


def parse(data):
    return data

def part1(data):
    elf = max([sum([int(x) for x in elf.split()]) for elf in data.split("\n\n")])
    return elf

def part2(data):
    elfs = sorted([sum([int(x) for x in elf.split()]) for elf in data.split("\n\n")], reverse=True)
    return sum(elfs[:3])


if __name__ == "__main__":
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        path = f"{Path(__file__).parent.name}/indata.txt"
    else:
        path = "indata.txt"
    
    with open(path, "r") as file:
        data = parse(file.read())
    
    print(part1(data))
    print(part2(data))