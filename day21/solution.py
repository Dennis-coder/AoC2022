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
            k: (int(v) if v.isnumeric() else v)
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
        x, op, y = data[node].split(" ")
        return int(eval(f"{calc(x)}{op}{calc(y)}"))
    
    return calc("root")

def part2(data):
    def calc(node):
        if isinstance(data[node], int):
            return data[node]
        x, op, y = data[node].split(" ")
        return int(eval(f"{calc(x)}{op}{calc(y)}"))
    
    def uses_human(node):
        if node == "humn":
            return True
        if isinstance(data[node], int):
            return False
        x, _, y = data[node].split(" ")
        if "humn" in (x, y):
            return True
        if uses_human(x):
            return True
        if uses_human(y):
            return True
        return False

    inverse_op = {
        "+": "-",
        "-": "+",
        "*": "/",
        "/": "*"
    }

    def needs_to_be(node, val):
        if node == "humn":
            return val
        x, op, y = data[node].split(" ")
        if uses_human(x):
            print(node, val, x, op, data[y])
            y = calc(y)
            x_val = eval(f"{val}{inverse_op[op]}{y}")
            return needs_to_be(x, x_val)
        elif uses_human(y):
            print(node, val, data[x], op, y)
            x = calc(x)
            y_val = eval(f"{val}{inverse_op[op]}{x}")
            return needs_to_be(y, y_val)

    for k in data.keys():
        if uses_human(k):
            continue
        else:
            data[k] = calc(k)

    x, _, y = data["root"].split(" ")
    if uses_human(x):
        return int(needs_to_be(x, calc(y)))
    elif uses_human(y):
        return int(needs_to_be(x, calc(x)))
    


    print(data)

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))

# < 9879574614298