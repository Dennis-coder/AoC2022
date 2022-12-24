from pathlib import Path
from queue import PriorityQueue
from functools import lru_cache


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = file.read().splitlines()
    
    start = (data[0].index("."), 0)
    goal = (data[-1].index("."), len(data) - 1)

    maze = [
        [
            1 if char == "#" else 0
            for char in row
        ]
        for row in data
    ]

    blizzards = [
        ((x, y), (1,0) if char == ">" else (-1,0) if char == "<" else (0,1) if char == "v" else (0,-1))
        for y, row in enumerate(data)
        for x, char in enumerate(row)
        if char in "<>^v"
    ]

    return maze, blizzards, start, goal

def manhattan(p, q):
    return abs(q[0] - p[1]) + abs(q[1] - p[1])

def moves(x, y):
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1

def astar(start, goal, maze, blizzards_start, start_minute):
    @lru_cache
    def blizzards(minute):
        return set([
            ((x+dx*minute-1)%(len(maze[0])-2)+1, (y+dy*minute-1)%(len(maze)-2)+1)
            for (x,y),(dx,dy) in blizzards_start
        ])

    pq = PriorityQueue()
    pq.put((manhattan(start, goal), *start, start_minute))
    visited = set()
    while not pq.empty():
        cost, x, y, minute = pq.get()

        if not (0 <= x < len(maze[0]) and 0 <= y < len(maze)) \
        or (x,y) in blizzards(minute) \
        or (x, y, minute) in visited \
        or maze[y][x]:
            continue
        
        visited.add((x, y, minute))

        if (x, y) == goal:
            return minute

        pq.put((cost+1, x, y, minute+1))
        for x2, y2 in moves(x, y):
            pq.put((
                manhattan((x2, y2), goal) + minute + 1,
                x2,
                y2,
                minute + 1
            ))

def part1(data):
    maze, blizzards_start, start, goal = data

    minutes = astar(start, goal, maze, blizzards_start, 0)
    
    return minutes

def part2(data):
    maze, blizzards_start, start, goal = data

    minutes = astar(start, goal, maze, blizzards_start, 0)
    minutes = astar(goal, start, maze, blizzards_start, minutes)
    minutes = astar(start, goal, maze, blizzards_start, minutes)
    
    return minutes


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))