from pathlib import Path


def parse(data):
    return [x.split() for x in data.split("\n")]

def part1(data):
    score = 0
    for op, you in data:
        if op == "A" and you == "X":
            score += 4
        elif op == "A" and you == "Y":
            score += 8
        elif op == "A" and you == "Z":
            score += 3
        elif op == "B" and you == "X":
            score += 1
        elif op == "B" and you == "Y":
            score += 5
        elif op == "B" and you == "Z":
            score += 9
        elif op == "C" and you == "X":
            score += 7
        elif op == "C" and you == "Y":
            score += 2
        elif op == "C" and you == "Z":
            score += 6
    return score

def part2(data):
    score = 0
    for op, you in data:
        if op == "A" and you == "X":
            score += 3
        elif op == "A" and you == "Y":
            score += 4
        elif op == "A" and you == "Z":
            score += 8
        elif op == "B" and you == "X":
            score += 1
        elif op == "B" and you == "Y":
            score += 5
        elif op == "B" and you == "Z":
            score += 9
        elif op == "C" and you == "X":
            score += 2
        elif op == "C" and you == "Y":
            score += 6
        elif op == "C" and you == "Z":
            score += 7
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