from pathlib import Path


def parse(data):
    pass

def part1(data):
    pass

def part2(data):
    pass


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