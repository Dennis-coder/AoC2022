from queue import Queue


def parse(file_name):
    with open(file_name, "r") as file:
        data = file.read().splitlines()
        
    start = [
        (x,y) 
        for y, line in enumerate(data) 
        for x, char in enumerate(line) 
        if char == "S"
    ][0]
    end = [
        (x,y) 
        for y, line in enumerate(data) 
        for x, char in enumerate(line) 
        if char == "E"
    ][0]
    height_map = [
        [
            0 if char == "S" else 25 if char == "E" else ord(char) - 97
            for char in line
        ]
        for line in data
    ]

    return start, end, height_map

def offsets(x, y):
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1

def part1(data):
    start, end, maze = data
    visited = set()
    bfs = Queue()
    bfs.put((*start, 0))
    while not bfs.empty():
        x, y, steps = bfs.get()
        if (x, y) in visited:
            continue
        if (x, y) == end:
            return steps

        visited.add((x, y))
        for x2, y2 in offsets(x, y):
            if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and maze[y][x] + 1 >= maze[y2][x2]:
                bfs.put((x2, y2, steps + 1))


def part2(data):
    _, end, maze = data
    visited = set()
    bfs = Queue()
    bfs.put((*end, 0))
    while not bfs.empty():
        x, y, steps = bfs.get()
        if (x, y) in visited:
            continue
        if maze[y][x] == 0:
            return steps

        visited.add((x, y))
        for x2, y2 in offsets(x, y):
            if 0 <= x2 < len(maze[0]) and 0 <= y2 < len(maze) and maze[y][x] <= maze[y2][x2] + 1:
                bfs.put((x2, y2, steps + 1))
