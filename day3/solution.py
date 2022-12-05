from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = file.read().split()
    return data
    
def part1(data):
    prio_sum = 0
    for bag in data:
        comp1 = set(bag[:len(bag) // 2])
        comp2 = set(bag[len(bag) // 2:])
        val = list(comp1.intersection(comp2))[0]
        prio_sum += ord(val) - (38 if ord(val) <= 90 else 96)
    return prio_sum

def part2(data):
    badge_sum = 0
    for i in range(0, len(data), 3):
        common = set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2]))
        val = ord(list(common)[0])
        badge_sum += val - (38 if val <= 90 else 96)
    return badge_sum


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))