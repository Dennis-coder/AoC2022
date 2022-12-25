import ast
from functools import cmp_to_key


def parse(file_name):
    with open(file_name, "r") as file:
        data = [
            [
                ast.literal_eval(val) 
                for val in pair.split("\n")
            ] 
            for pair in file.read().split("\n\n")
        ]
    return data

def is_ordered(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 0 if left == right else 1
    if isinstance(left, int):
        return is_ordered([left], right)
    if isinstance(right, int):
        return is_ordered(left, [right])

    i = 0
    while i < len(left) and i < len(right):
        res = is_ordered(left[i], right[i])
        if res != 0:
            return res
        i += 1
    if i == len(left) and i == len(right):
        return 0
    if i == len(left):
        return -1
    if i == len(right):
        return 1

def part1(data):
    sum_of_indices = 0
    for i, (left, right) in enumerate(data):
        if is_ordered(left, right) == -1:
            sum_of_indices += i + 1
    return sum_of_indices
        
def part2(data):
    packet_1 = [[2]]
    packet_2 = [[6]]
    l = [packet_1, packet_2]
    for pair in data:
        l += pair
    l.sort(key=cmp_to_key(is_ordered))
    return (l.index(packet_1)+1) * (l.index(packet_2)+1)
