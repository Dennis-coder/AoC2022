from pathlib import Path


def parse(data):
    return [(ord(x[0])-65, ord(x[2])-88) for x in data.split("\n")]

def part1(data):
    score = 0
    for op, you in data:
        score += (you + 1)
        if (op + 1) % 3 == you:
            score += 6
        elif op == you:
            score += 3
    return score

def part2(data):
    score = 0
    for op, res in data:
        score += res * 3
        if res == 2:
            score += (op + 1) % 3 + 1
        elif res == 1:
            score += op + 1
        else:
            score += (op - 1) % 3 + 1
    return score


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