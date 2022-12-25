def parse(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return data

def part1(data):
    for i in range(len(data)):
        if len(set(data[i-4:i])) == 4:
            return i

def part2(data):
    for i in range(len(data)):
        if len(set(data[i-14:i])) == 14:
            return i
