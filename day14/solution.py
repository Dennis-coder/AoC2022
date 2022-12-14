from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [[[int(coord) for coord in coords.split(",")] for coords in  row.split(" -> ")] for row in file.read().split("\n")]
    return data

def part1(data):
    cave = {(500, 0): 0}
    for path in data:
        start_x, start_y = path[0]
        for end_x, end_y in path[1:]:
            if start_x == end_x:
                x = start_x
                for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    cave[(x, y)] = 1
            if start_y == end_y:
                y = start_y
                for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                    cave[(x, y)] = 1
            start_x, start_y = end_x, end_y
    
    units_of_sand = 0
    x1 = min([el[0] for el in cave])
    x2 = max([el[0] for el in cave])
    y1 = min([el[1] for el in cave])
    y2 = max([el[1] for el in cave])
    while True:
        sand_x, sand_y = 500, 0
        while True:
            if not (x1 <= sand_x <= x2 and y1 <= sand_y <= y2):
                break

            if (sand_x, sand_y + 1) not in cave:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in cave:
                sand_x -= 1
                sand_y += 1
            elif (sand_x + 1, sand_y + 1) not in cave:
                sand_x += 1
                sand_y += 1
            else:
                break
        
        if x1 <= sand_x <= x2 and y1 <= sand_y <= y2:
            cave[(sand_x, sand_y)] = 2
            units_of_sand += 1
        else:
            break

    return units_of_sand

def part2(data):
    cave = {(500, 0): 0}
    for path in data:
        start_x, start_y = path[0]
        for end_x, end_y in path[1:]:
            if start_x == end_x:
                x = start_x
                for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    cave[(x, y)] = 1
            if start_y == end_y:
                y = start_y
                for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                    cave[(x, y)] = 1
            start_x, start_y = end_x, end_y
    
    units_of_sand = 0
    floor = max([el[1] for el in cave]) + 2
    while True:
        sand_x, sand_y = 500, 0
        while True:
            if sand_y + 1 == floor:
                break

            if (sand_x, sand_y + 1) not in cave:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in cave:
                sand_x -= 1
                sand_y += 1
            elif (sand_x + 1, sand_y + 1) not in cave:
                sand_x += 1
                sand_y += 1
            else:
                break
        
        cave[(sand_x, sand_y)] = 2
        units_of_sand += 1
        
        if sand_x == 500 and sand_y == 0:
            break
        

    vizualize_cave(cave)
    return units_of_sand


def vizualize_cave(cave):
    x1 = min([el[0] for el in cave])
    x2 = max([el[0] for el in cave])
    y1 = min([el[1] for el in cave])
    y2 = max([el[1] for el in cave])

    for y in range(y1, y2 + 1):
        row = ""
        for x in range(x1, x2 + 1):
            if (x, y) not in  cave:
                row += " "
            elif cave[(x, y)] == 1:
                row += "#"
            elif cave[(x, y)] == 2:
                row += "o"
        print(row)


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))