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
        row[1] = int(row[1])
    return data

def part1(data):
    hx = hy = tx = ty = 0
    visited = {(tx, ty)}
    switch = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    for dir, n in data:
        dx, dy = switch[dir]
        for _ in range(n):
            hx += dx
            hy += dy
            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                tx = hx - dx
                ty = hy - dy
                visited.add((tx, ty))
    return len(visited)

def part2(data):
    knots = [[0,0] for _ in range(10)]
    visited = {(0,0)}
    head = knots[0]
    switch = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    for dir, n in data:
        for _ in range(n):
            dx, dy = switch[dir]
            head[0] += dx
            head[1] += dy
            prev_x, prev_y = head
            for knot in knots[1:]:
                dx = (prev_x - knot[0]) // 2 if abs(prev_x - knot[0]) > 1 else 0
                dy = (prev_y - knot[1]) // 2 if abs(prev_y - knot[1]) > 1 else 0
                if dx or dy:
                    knot[0] = prev_x - dx
                    knot[1] = prev_y - dy
                prev_x, prev_y = knot
            visited.add((prev_x, prev_y))
    
    return len(visited)

def vizualize_knots(knots):
    x0 = min([el[0] for el in knots])
    x1 = max([el[0] for el in knots])
    y0 = min([el[1] for el in knots])
    y1 = max([el[1] for el in knots])
    for y in range(y1, y0 - 1, -1):
        row = ""
        for x in range(x0, x1 + 1):
            if [x, y] in knots:
                row += "#"
            else:
                row += "."
        print(row)

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))