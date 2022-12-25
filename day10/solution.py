def parse(file_name):
    with open(file_name, "r") as file:
        data = [
            (row, 0) if len(row) == 1 else (row[0], int(row[1]))
            for row in [
                row.split() 
                for row in file.read().splitlines()
            ]
        ]
    return data

def calc_x_vals(data):
    x = 1
    x_vals = []
    for op, val in data:
        x_vals.append(x)
        if op == "addx":
            x_vals.append(x)
        x += val
    x_vals.append(x)
    return x_vals

def part1(data):
    return sum([x * (i+1) for i, x in enumerate(calc_x_vals(data)) if (i+1) % 40 == 20])

def part2(data):
    x_vals = calc_x_vals(data)
    return "\n" + "\n".join([
        "".join([
            "#" if abs(x - x_vals[y * 40 + x]) <= 1 else " "
            for x in range(40)
        ])
        for y in range(len(x_vals) // 40)
    ])
