from pathlib import Path
import re


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [
            ((int(matches[0]), int(matches[1])), (int(matches[2]), int(matches[3])))
            for matches in (
                re.findall("-?\d+", line)
                for line in file.read().split("\n")
            )
        ]
    return data

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def part1(data):
    cannot_contain = set()
    sensors = set([sensor for sensor, _ in data])
    beacons = set([beacon for _, beacon in data])
    y = 2000000
    for sensor, closest_beacon in data:
        max_distance = manhattan(sensor, closest_beacon)
        distance_to_y = abs(y - sensor[1])
        if distance_to_y > max_distance:
            continue
        steps = max_distance - distance_to_y
        for x in range(sensor[0] - steps, sensor[0] + steps + 1):
            cannot_contain.add((x, y))
    return len(cannot_contain.difference(sensors, beacons))
            

def part2(data):
    can_contain = set()
    max_val = 4000000
    for sensor, closest_beacon in data:
        distance = manhattan(sensor, closest_beacon) + 1
        for y in range(max(0, sensor[1] - distance), min(max_val, sensor[1] + distance + 1)):
            steps_x = distance - abs(y - sensor[1])
            if 0 <= sensor[0] - steps_x <= max_val:
                can_contain.add((sensor[0] - steps_x, y))
            if 0 <= sensor[0] + steps_x <= max_val:
                can_contain.add((sensor[0] + steps_x, y))
    
    for sensor, closest_beacon in data:
        distance = manhattan(sensor, closest_beacon)
        can_contain = {possible_pos for possible_pos in can_contain if distance < manhattan(sensor, possible_pos)}

    x, y = list(can_contain)[0]
    return x * 4000000 + y


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))