from pathlib import Path


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = {
            k: (int(v) if v.isnumeric() else v.replace("/", "//").split(" "))
            for k, v in [
                line.split(": ") 
                for line in file.read().splitlines()
            ]
        }
    return data

def part1(data):
    def calc(node):
        if isinstance(data[node], int):
            return data[node]
        x, op, y = data[node]
        return int(eval(f"{calc(x)}{op}{calc(y)}"))
    return calc("root")

def part2(data):
    def calc(node):
        if isinstance(data[node], int):
            return data[node]
        x, op, y = data[node]
        return int(eval(f"{calc(x)}{op}{calc(y)}"))
    
    def uses_human(node):
        if node == "humn":
            return True
        if isinstance(data[node], int):
            return False
        x, _, y = data[node]
        if "humn" in (x, y) or uses_human(x) or uses_human(y):
            return True
        return False

    def calc_humn(node, val):
        if node == "humn":
            return val
        x, op, y = data[node]
        if uses_human(x):
            y = calc(y)
            x_val = eval(f"{val}{inverse_op[op]}{y}")
            return calc_humn(x, x_val)
        elif uses_human(y):
            x = calc(x)
            if op == "-":
                y_val = eval(f"{x}{op}{val}")
            else:
                y_val = eval(f"{val}{inverse_op[op]}{x}")
            return calc_humn(y, y_val)

    inverse_op = {
        "+": "-",
        "-": "+",
        "*": "//",
        "//": "*"
    }

    x, _, y = data["root"]
    if uses_human(x):
        return int(calc_humn(x, calc(y)))
    elif uses_human(y):
        return int(calc_humn(y, calc(x)))

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))