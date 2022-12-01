from pathlib import Path


def refactor_data(data):
    return data

def part_1(data):
    calories = max([sum([int(x) for x in elf.split()]) for elf in data.split("\n\n")])
    return calories

def part_2(data):
    calories = sorted([sum([int(x) for x in elf.split()]) for elf in data.split("\n\n")])
    return sum(calories[-3:])


if __name__ == "__main__":
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        path = f"{Path(__file__).parent.name}/indata.txt"
    else:
        path = "indata.txt"
    
    with open(path, "r") as file:
        data = refactor_data(file.read())
    
    print(part_1(data))
    print(part_2(data))