def parse(file_name):
    with open(file_name, "r") as file:
        data = [
            sum([int(x) for x in elf.split()]) 
            for elf in file.read().split("\n\n")
        ]
    return data

def part1(data):
    elf = max(data)
    return elf

def part2(data):
    elfs = sorted(data, reverse=True)
    return sum(elfs[:3])
