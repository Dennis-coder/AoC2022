from pathlib import Path


def parse(data):
    return [(x[:len(x) // 2], x[len(x) // 2 :]) for x in data.split()]
    

def part1(data):
    prio_sum = 0
    for comp1, comp2 in data:
        common = [ord(x) for x in set(comp1).intersection(set(comp2))]
        for val in common:
            if 65 <= val <= 90:
                prio_sum += val - 64 + 26
            if 97 <= val <= 122:
                prio_sum += val - 96
    return prio_sum

def part2(data):
    badge_sum = 0
    for i in range(0, len(data), 3):
        common = set(data[i][0] + data[i][1])
        for comp1, comp2 in data[i+1:i+3]:
            common = common.intersection(set(comp1 + comp2))
        val = ord(list(common)[0])
        if 65 <= val <= 90:
            badge_sum += val - 64 + 26
        if 97 <= val <= 122:
            badge_sum += val - 96
    return badge_sum


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