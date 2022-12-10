from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [row.split() for row in file.read().split("\n")]
    for row in data:
        if len(row) > 1:
            row[1] = int(row[1])
        else:
            row.append(0)
    return data

def part1(data):
    x = 1
    x_vals = [1]
    for op, val in data:
        x_vals.append(x)
        if op == "addx":
            x_vals.append(x)
        x += val
    return sum([x * i for i, x in enumerate(x_vals) if i % 40 == 20])

def part2(data):
    x = 1
    x_vals = []
    for op, val in data:
        x_vals.append(x)
        if op == "addx":
            x_vals.append(x)
        x += val

    res = "\n"
    for y in range(len(x_vals) // 40):
        for x in range(40):
            res += "#" if abs(x - x_vals[y * 40 + x]) <= 1 else " "
        res += "\n"

    return res


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))