import re
from math import sqrt


def parse(file_name):
    with open(file_name, "r") as file:
        map_str, directions = file.read().split("\n\n")

    directions = [
        int(el) if el.isnumeric() else el
        for el in re.findall("\d+|\D+", directions)
    ]
    pane_size = int(sqrt(sum([len(line.strip()) for line in map_str.splitlines()]) // 6))
    panes = []
    coords = []
    temp_map = map_str.splitlines()
    for j in range(len(temp_map) // pane_size):
        for i in range(len(temp_map[j * pane_size]) // pane_size):
            if temp_map[j * pane_size][i * pane_size] == " ":
                continue
            coords.append((i*pane_size, j*pane_size))
            panes.append(set([
                (x, y)
                for y, row in enumerate(temp_map[j * pane_size : (j+1) * pane_size])
                for x, char in enumerate(row[i * pane_size : (i+1) * pane_size])
                if char == "#"
            ]))

    return panes, coords, directions, pane_size

def rotate_pos(x, y, relative_dir, pane_size):
    if relative_dir == 0:
        return x, y
    if relative_dir == 1:
        return y, pane_size - x - 1
    if relative_dir == 2:
        return pane_size - x - 1, pane_size - y - 1
    if relative_dir == 3:
        return pane_size - y - 1, x

def move(x, y, facing):
    if facing == 0: # Go right
        return x+1, y

    if facing == 1: # Go down
        return x, y+1

    if facing == 2: # Go left
        return x-1, y

    if facing == 3: # Go up
        return x, y-1

def run(directions, panes, wrapping, pane_size):
    x, y, facing, cur_pane, pane_idx = 0, 0, 0, panes[0], 0
    for dir in directions:
        if dir == "R":
            facing = (facing+1) % 4
            continue
        if dir == "L":
            facing = (facing-1) % 4
            continue

        for _ in range(dir):
            new_x, new_y = move(x, y, facing)

            if (new_x, new_y) in cur_pane:
                break

            if 0 <= new_x < pane_size and 0 <= new_y < pane_size:
                x, y = new_x, new_y
                continue

            new_pane_idx, relative_dir = wrapping[pane_idx][facing]
            new_x, new_y = rotate_pos(new_x % pane_size, new_y % pane_size, relative_dir, pane_size)

            if (new_x, new_y) in panes[new_pane_idx]:
                break
            
            x, y = new_x, new_y
            facing = (facing - relative_dir) % 4
            cur_pane = panes[new_pane_idx]
            pane_idx = new_pane_idx

    return x, y, facing, pane_idx

def part1(data):
    panes, coords, directions, pane_size = data

    wrapping = [
        [(1,0), (2,0), (1,0), (4,0)],
        [(0,0), (1,0), (0,0), (1,0)],
        [(2,0), (4,0), (2,0), (0,0)],
        [(4,0), (5,0), (4,0), (5,0)],
        [(3,0), (0,0), (3,0), (2,0)],
        [(5,0), (3,0), (5,0), (3,0)]
    ]

    # test_wrapping = [
    #     [(0,0), (3,0), (0,0), (4,0)],
    #     [(2,0), (1,0), (3,0), (1,0)],
    #     [(3,0), (2,0), (1,0), (2,0)],
    #     [(1,0), (4,0), (2,0), (0,0)],
    #     [(5,0), (0,0), (5,0), (3,0)],
    #     [(4,0), (5,0), (4,0), (5,0)]
    # ]

    x, y, facing, pane = run(directions, panes, wrapping, pane_size)
    dx, dy = coords[pane]

    return 1000 * (y+dy+1) + 4 * (x+dx+1) + facing

def part2(data):
    panes, coords, directions, pane_size = data

    wrapping = [
        [(1,0), (2,0), (3,2), (5,3)],
        [(4,2), (2,3), (0,0), (5,0)],
        [(1,1), (4,0), (3,1), (0,0)],
        [(4,0), (5,0), (0,2), (2,3)],
        [(1,2), (5,3), (3,0), (2,0)],
        [(4,1), (1,0), (0,1), (3,0)]
    ]

    # test_wrapping = [
    #     [(5,2), (3,0), (2,1), (1,2)],
    #     [(2,0), (4,2), (5,3), (0,2)],
    #     [(3,0), (4,1), (1,0), (0,3)],
    #     [(5,3), (4,0), (2,0), (0,0)],
    #     [(5,0), (1,2), (2,3), (3,0)],
    #     [(0,2), (1,1), (4,0), (3,1)]
    # ]

    x, y, facing, pane = run(directions, panes, wrapping, pane_size)
    dx, dy = coords[pane]
    return 1000 * (y+dy+1) + 4 * (x+dx+1) + facing
