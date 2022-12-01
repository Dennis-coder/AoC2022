from pathlib import Path


def refactor_data(data):
    pass

def part_1(data):
    pass

def part_2(data):
    pass


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