from pathlib import Path
import re


PANE_SIZE = 50
class Pane:
    def __init__(self, pane, x, y):
        self.pane = pane
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.go_left = lambda y: (PANE_SIZE - 1, y, 2)
        self.go_right = lambda y: (0, y, 0)
        self.go_up = lambda x: (x, PANE_SIZE - 1, 3)
        self.go_down = lambda x: (x, 0, 1)
    
    def __str__(self):
        return f"({self.i}, {self.j})"

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        map_str, directions = file.read().split("\n\n")

    directions = [
        int(el) if el.isnumeric() else el
        for el in re.findall("\d+|\D+", directions)
    ]
    
    panes = []
    temp_map = map_str.splitlines()
    for i in range(len(temp_map) // PANE_SIZE):
        for j in range(len(temp_map[i * PANE_SIZE]) // PANE_SIZE):
            if temp_map[i * PANE_SIZE][j * PANE_SIZE] == " ":
                continue
            panes.append(Pane([
                row[j * PANE_SIZE : (j+1) * PANE_SIZE]
                for row in temp_map[i * PANE_SIZE : (i+1) * PANE_SIZE]
            ], j*PANE_SIZE, i*PANE_SIZE))

    return panes, directions

turn_left = {
    0: 3,
    1: 0,
    2: 1,
    3: 2
}

turn_right = {
    0: 1,
    1: 2,
    2: 3,
    3: 0
}

def run(directions, start_pane):
    x, y, facing, cur_pane = 0, 0, 0, start_pane
    for dir in directions:
        if dir == "R":
            facing = turn_right[facing]
            continue
        if dir == "L":
            facing = turn_left[facing]
            continue

        for _ in range(dir):
            if facing == 0: # Go right
                new_x = x + 1
                x1, y1, _ = cur_pane.go_right(y)
                if (new_x == PANE_SIZE and cur_pane.right.pane[y1][x1] == "#") \
                or (new_x < PANE_SIZE and cur_pane.pane[y][new_x] == "#"):
                    break
                x = new_x
                if x == PANE_SIZE:
                    x, y, facing = cur_pane.go_right(y)
                    cur_pane = cur_pane.right

            elif facing == 1: # Go down
                new_y = y + 1
                x1, y1, _ = cur_pane.go_down(x)
                if (new_y == PANE_SIZE and cur_pane.down.pane[y1][x1] == "#") \
                or (new_y < PANE_SIZE and cur_pane.pane[new_y][x] == "#"):
                    break
                y = new_y
                if y == PANE_SIZE:
                    x, y, facing = cur_pane.go_down(x)
                    cur_pane = cur_pane.down

            elif facing == 2: # Go left
                new_x = x - 1
                x1, y1, _ = cur_pane.go_left(y)
                if (new_x == -1 and cur_pane.left.pane[y1][x1] == "#") \
                or (new_x >= 0 and cur_pane.pane[y][new_x] == "#"):
                    break
                x = new_x
                if x == -1:
                    x, y, facing = cur_pane.go_left(y)
                    cur_pane = cur_pane.left

            elif facing == 3: # Go up
                new_y = y - 1
                x1, y1, _ = cur_pane.go_up(x)
                if (new_y == -1 and cur_pane.up.pane[y1][x1] == "#") \
                or (new_y >= 0 and cur_pane.pane[new_y][x] == "#"):
                    break
                y = new_y
                if y == -1:
                    x, y, facing = cur_pane.go_up(x)
                    cur_pane = cur_pane.up
    return x, y, facing, cur_pane

def part1(data):
    panes, directions = data
    
    panes[0].right = panes[1]
    panes[0].left  = panes[1]
    panes[0].up    = panes[4]
    panes[0].down  = panes[2]
    
    panes[1].right = panes[0]
    panes[1].left  = panes[0]
    panes[1].up    = panes[1]
    panes[1].down  = panes[1]
    
    panes[2].right = panes[2]
    panes[2].left  = panes[2]
    panes[2].up    = panes[0]
    panes[2].down  = panes[4]
    
    panes[3].right = panes[4]
    panes[3].left  = panes[4]
    panes[3].up    = panes[5]
    panes[3].down  = panes[5]
    
    panes[4].right = panes[3]
    panes[4].left  = panes[3]
    panes[4].up    = panes[2]
    panes[4].down  = panes[0]
    
    panes[5].right = panes[5]
    panes[5].left  = panes[5]
    panes[5].up    = panes[3]
    panes[5].down  = panes[3]

    x, y, facing, cur_pane = run(directions, panes[0])
    
    return 1000 * (cur_pane.y+y+1) + 4 * (cur_pane.x+x+1) + facing

def part2(data):
    panes, directions = data
    
    panes[0].right = panes[1]
    panes[0].go_right = lambda y: (0, y, 0)
    panes[0].left  = panes[3]
    panes[0].go_left = lambda y: (0, PANE_SIZE - y - 1, 0)
    panes[0].up    = panes[5]
    panes[0].go_up = lambda x: (0, x, 0)
    panes[0].down  = panes[2]
    panes[0].go_down = lambda x: (x, 0, 1)
    
    panes[1].right = panes[4]
    panes[1].go_right = lambda y: (PANE_SIZE - 1, PANE_SIZE - y - 1, 2)
    panes[1].left  = panes[0]
    panes[1].go_left = lambda y: (PANE_SIZE - 1, y, 2)
    panes[1].up    = panes[5]
    panes[1].go_up = lambda x: (x, PANE_SIZE - 1, 3)
    panes[1].down  = panes[2]
    panes[1].go_down = lambda x: (PANE_SIZE - 1, x, 2)
    
    panes[2].right = panes[1]
    panes[2].go_right = lambda y: (y, PANE_SIZE - 1, 3)
    panes[2].left  = panes[3]
    panes[2].go_left = lambda y: (y, 0, 1)
    panes[2].up    = panes[0]
    panes[2].go_up = lambda x: (x, PANE_SIZE - 1, 3)
    panes[2].down  = panes[4]
    panes[2].go_down = lambda x: (x, 0, 1)
    
    panes[3].right = panes[4]
    panes[3].go_right = lambda y: (0, y, 0)
    panes[3].left  = panes[0]
    panes[3].go_left = lambda y: (0, PANE_SIZE - y - 1, 0)
    panes[3].up    = panes[2]
    panes[3].go_up = lambda x: (0, x, 0)
    panes[3].down  = panes[5]
    panes[3].go_down = lambda x: (x, 0, 1)
    
    panes[4].right = panes[1]
    panes[4].go_right = lambda y: (PANE_SIZE - 1, PANE_SIZE - y - 1, 2)
    panes[4].left  = panes[3]
    panes[4].go_left = lambda y: (PANE_SIZE - 1, y, 2)
    panes[4].up    = panes[2]
    panes[4].go_up = lambda x: (x, PANE_SIZE - 1, 3)
    panes[4].down  = panes[5]
    panes[4].go_down = lambda x: (PANE_SIZE - 1, x, 2)
    
    panes[5].right = panes[4]
    panes[5].go_right = lambda y: (y, PANE_SIZE - 1, 3)
    panes[5].left  = panes[0]
    panes[5].go_left = lambda y: (y, 0, 1)
    panes[5].up    = panes[3]
    panes[5].go_up = lambda x: (x, PANE_SIZE - 1, 3)
    panes[5].down  = panes[1]
    panes[5].go_down = lambda x: (x, 0, 1)

    x, y, facing, cur_pane = run(directions, panes[0])
    return 1000 * (cur_pane.y+y+1) + 4 * (cur_pane.x+x+1) + facing


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))