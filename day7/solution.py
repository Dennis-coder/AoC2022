def parse(file_name):
    with open(file_name, "r") as file:
        data = [row.split() for row in file.read().split("\n")]

    tree = []
    sizes = {}
    for row in data:
        if row[1] == "cd":
            if row[2] == "..":
                tree.pop()
            else:
                path = (tree[-1] + "/" if tree else "") + row[2]
                tree.append(path)
                sizes[path] = 0

        elif row[0].isnumeric():
            file_size = int(row[0])
            for node in tree:
                sizes[node] += file_size

    return sizes

def part1(nodes):
    return sum([node for node in nodes.values() if node <= 100000])

def part2(nodes):
    needed = nodes["/"] - 40000000
    return min([node for node in nodes.values() if node > needed])
