def parse(file_name):
    with open(file_name, "r") as file:
        nodes = {
            k: (int(v) if v.isnumeric() else v.replace("/", "//").split(" "))
            for k, v in [
                line.split(": ") 
                for line in file.read().splitlines()
            ]
        }
    return nodes

def calc(node, nodes):
    if isinstance(nodes[node], int):
        return nodes[node]
    x, op, y = nodes[node]
    return int(eval(f"{calc(x, nodes)}{op}{calc(y, nodes)}"))

def uses_human(node, nodes):
    if node == "humn":
        return True
    if isinstance(nodes[node], int):
        return False
    x, _, y = nodes[node]
    if "humn" in (x, y) or uses_human(x, nodes) or uses_human(y, nodes):
        return True
    return False

def calc_humn(node, val, nodes):
    inverse_op = {
        "+": "-",
        "-": "+",
        "*": "//",
        "//": "*"
    }
    if node == "humn":
        return val
    x, op, y = nodes[node]
    if uses_human(x, nodes):
        y = calc(y, nodes)
        x_val = eval(f"{val}{inverse_op[op]}{y}")
        return calc_humn(x, x_val, nodes)
    elif uses_human(y, nodes):
        x = calc(x, nodes)
        if op == "-":
            y_val = eval(f"{x}{op}{val}")
        else:
            y_val = eval(f"{val}{inverse_op[op]}{x}")
        return calc_humn(y, y_val, nodes)

def part1(data):
    return calc("root", data)

def part2(data):    
    x, _, y = data["root"]
    if uses_human(x, data):
        return int(calc_humn(x, calc(y, data), data))
    elif uses_human(y, data):
        return int(calc_humn(y, calc(x, data), data))
