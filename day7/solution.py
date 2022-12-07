from pathlib import Path


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = None
    
    def set_sizes(self):
        size = 0
        for child in self.children.values():
            if isinstance(child, Node):
                child.set_sizes()
            size += child.size
        self.size = size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [row.split() for row in file.read().split("\n")]
    root = Node("/", None)
    cur = root
    i = 0;
    while i < len(data):
        if data[i][1] == "cd":
            if data[i][2] == "/":
                cur = root
            elif data[i][2] == "..":
                cur = cur.parent
            else:
                cur = cur.children[data[i][2]]
            i += 1
        elif data[i][1] == "ls":
            i += 1
            while i < len(data) and data[i][0] != "$":
                if data[i][0] == "dir":
                    node = Node(data[i][1], cur)
                    cur.children[node.name] = node
                elif data[i][0].isnumeric():
                    file = File(data[i][1], int(data[i][0]))
                    cur.children[file.name] = file
                i += 1  
    root.set_sizes()
    return root

def part1(root):
    nodes = []
    part1_inner(root, nodes)
    return sum([node.size for node in nodes])

def part1_inner(node, nodes):
    if node.size <= 100000:
        nodes.append(node)
    for child in node.children.values():
        if isinstance(child, Node):
            part1_inner(child, nodes)

def part2(root):
    nodes = []
    needed = root.size - (70000000 - 30000000)
    print(needed)
    part2_inner(root, nodes)
    best = root
    for node in nodes:
        if node.size - needed < 0:
            continue
        if node.size < best.size:
            best = node
    return best.size

def part2_inner(node, nodes):
    nodes.append(node)
    for child in node.children.values():
        if isinstance(child, Node):
            part2_inner(child, nodes)


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))