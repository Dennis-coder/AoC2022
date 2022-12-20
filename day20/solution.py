from pathlib import Path


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [int(x) for x in file.read().splitlines()]
    nodes = {(i,val):Node(val) for i, val in enumerate(data)}
    return nodes, data

def reset_nodes(nodes, order):
    start = nodes[(0, order[0])]
    prev = start
    for i, val in enumerate(order[1:]):
        node = nodes[(i+1, val)]
        node.prev = prev
        prev.next = node
        prev = node
    start.prev = prev
    prev.next = start

def mix(nodes, order):
    length = len(order) - 1
    for i, val in enumerate(order):
        key = (i,val)
        node = nodes[key]
        n = val%length
        if n == 0:
            continue
        
        temp = node
        for _ in range(n):
            temp = temp.next
        prev = temp
        next = temp.next
        
        # Cut out the node
        node.prev.next = node.next
        node.next.prev = node.prev

        # Paste it back in
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

def sum_grove_coordinates(nodes, order):
    idx = [i for i, val in enumerate(order) if val == 0][0]
    node = nodes[(idx, 0)]
    sum = 0
    for i in range(3000):
        node = node.next
        if (i+1) % 1000 == 0:
            sum += node.val
    return sum

def part1(data):
    nodes, order = data
    reset_nodes(nodes, order)
    mix(nodes, order)
    return sum_grove_coordinates(nodes, order)


def part2(data):
    nodes, order = data
    reset_nodes(nodes, order)

    order = [811589153 * val for val in order]
    nodes = {(i, val * 811589153):node for (i, val), node in nodes.items()}
    for (_, val), node in nodes.items():
        node.val = val

    for _ in range(10):
        mix(nodes, order)

    return sum_grove_coordinates(nodes, order)


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))