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
        data = file.read()
    height_map = []
    start = end = None
    for y, line in enumerate(data.split("\n")):
        row = []
        for x, char in enumerate(line):
            if char == "S":
                start = (x,y)
                row.append(0)
            elif char == "E":
                end = (x,y)
                row.append(25)
            else:
                row.append(ord(char) - 97)
        height_map.append(row)
    return (start, end, height_map)

def part1(data):
    start, end, maze = data
    visited = set()
    bfs = Queue()
    bfs.put((*start, 0))
    while bfs.qsize():
        x, y, steps = bfs.get()
        if (x, y) in visited:
            continue
        if (x, y) == end:
            return steps

        visited.add((x, y))
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in offsets:
            if 0 <= (x + dx) < len(maze[0]) and 0 <= (y + dy) < len(maze) and maze[y][x] + 1 >= maze[y + dy][x + dx]:
                bfs.put((x + dx, y + dy, steps + 1))


def part2(data):
    _, end, maze = data
    visited = set()
    bfs = Queue()
    bfs.put((*end, 0))
    while bfs.qsize():
        x, y, steps = bfs.get()
        if (x, y) in visited:
            continue
        if maze[y][x] == 0:
            return steps

        visited.add((x, y))
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in offsets:
            if 0 <= (x + dx) < len(maze[0]) and 0 <= (y + dy) < len(maze) and maze[y][x] <= maze[y + dy][x + dx] + 1:
                bfs.put((x + dx, y + dy, steps + 1))


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))