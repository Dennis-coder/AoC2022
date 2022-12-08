from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [[int(x) for x in row] for row in file.read().split("\n")]
    return data

def part1(data):
    visible = set()

    for y in range(len(data)):
        prev_h = -1
        for x in range(len(data[0])):
            if data[y][x] > prev_h:
                visible.add((x,y))
            prev_h = max(prev_h, data[y][x])
        prev_h = -1
        for x in range(len(data[0]) - 1, -1, -1):
            if data[y][x] > prev_h:
                visible.add((x,y))
            prev_h = max(prev_h, data[y][x])

    for x in range(len(data[0])):
        prev_h = -1
        for y in range(len(data)):
            if data[y][x] > prev_h:
                visible.add((x,y))
            prev_h = max(prev_h, data[y][x])
        prev_h = -1
        for y in range(len(data) - 1, -1, -1):
            if data[y][x] > prev_h:
                visible.add((x,y))
            prev_h = max(prev_h, data[y][x])
    return len(visible)

def part2(data):
    best_score = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            cur = data[y][x]
            score = 1
            for y2 in range(y - 1, -1, -1):
                if data[y2][x] >= cur or y2 == 0:
                    score *= abs(y - y2)
                    break
            for y2 in range(y + 1, len(data)):
                if data[y2][x] >= cur or y2 == len(data) - 1:
                    score *= abs(y - y2)
                    break
            for x2 in range(x - 1, -1, -1):
                if data[y][x2] >= cur or x2 == 0:
                    score *= abs(x - x2)
                    break
            for x2 in range(x + 1, len(data[0])):
                if data[y][x2] >= cur or x2 == len(data[0]) - 1:
                    score *= abs(x - x2)
                    break
            best_score = max(best_score, score)
    
    return best_score


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))