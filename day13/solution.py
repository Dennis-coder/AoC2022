from pathlib import Path
import ast


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [[ast.literal_eval(val) for val in pair.split("\n")] for pair in file.read().split("\n\n")]
    return data

def part1(data):
    sum_of_indices = 0
    for i, (left, right) in enumerate(data):
        if is_ordered(left, right):
            sum_of_indices += i + 1
    return sum_of_indices

def is_ordered(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else 2 if left == right else 0
    if isinstance(left, int):
        return is_ordered([left], right)
    if isinstance(right, int):
        return is_ordered(left, [right])

    i = 0
    while i < len(left) and i < len(right):
        res = is_ordered(left[i], right[i])
        if res != 2:
            return res
        i += 1
    if i == len(left) and i == len(right):
        return 2
    if i == len(left):
        return 1
    if i == len(right):
        return 0
        
def part2(data):
    divider_packet_1 = [[2]]
    divider_packet_2 = [[6]]
    flat_list = [divider_packet_1, divider_packet_2]
    for pair in data:
        flat_list += pair
    
    for i in range(len(flat_list)):
        for j in range(i - 1, -1, -1):
            if is_ordered(flat_list[j], flat_list[j + 1]):
                break
            flat_list[j], flat_list[j + 1] = flat_list[j + 1], flat_list[j]
    
    return (flat_list.index(divider_packet_1) + 1) * (flat_list.index(divider_packet_2) + 1)


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))