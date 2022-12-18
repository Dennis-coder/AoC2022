from pathlib import Path
from queue import Queue


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = set([tuple([int(x) for x in line.split(",")]) for line in file.read().split("\n")])
    return data

def neighbours(point):
    return (
        (point[0]-1, point[1],   point[2]),
        (point[0]+1, point[1],   point[2]),
        (point[0],   point[1]-1, point[2]),
        (point[0],   point[1]+1, point[2]),
        (point[0],   point[1],   point[2]-1),
        (point[0],   point[1],   point[2]+1)
    )

def part1(data):
    return sum([
        1 
        for point in data
        for neighbour in neighbours(point)
        if neighbour not in data
    ])

def part2(data):
    count = 0
    x1 = min([x for x, _, _ in data]) - 1
    x2 = max([x for x, _, _ in data]) + 1
    y1 = min([y for _, y, _ in data]) - 1
    y2 = max([y for _, y, _ in data]) + 1
    z1 = min([z for _, _, z in data]) - 1
    z2 = max([z for _, _, z in data]) + 1
    visited = set()
    bfs = Queue()
    bfs.put((x1, y1, z1))
    while not bfs.empty():
        cur = bfs.get()
        if cur in data:
            count += 1
            continue
        if cur in visited:
            continue
        x, y, z = cur
        if not (x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2):
            continue
        visited.add(cur)
        for neighbour in neighbours(cur):
            bfs.put(neighbour)
    return count

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))