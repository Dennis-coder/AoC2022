def parse(file_name):
    with open(file_name, "r") as file:
        data = [
            (dir, int(n))
            for dir, n in [
                row.split() 
                for row in file.read().splitlines()
            ]
        ]
    return data

def simulate(knots_amount, data):
    knots = [[0,0] for _ in range(knots_amount)]
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

def part1(data):
    return simulate(2, data)

def part2(data):
    return simulate(10, data)
