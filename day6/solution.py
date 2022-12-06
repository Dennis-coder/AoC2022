from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = file.read()
    return data

def part1(data):
    for i in range(len(data)):
        if len(set(data[i-4:i])) == 4:
            return i

def part2(data):
    for i in range(len(data)):
        if len(set(data[i-14:i])) == 14:
            return i


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))