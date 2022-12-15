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

def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = [sorted_intervals[0]]
    for i in sorted_intervals[1:]:
        if merged_intervals[-1][0] <= i[0] <= merged_intervals[-1][-1]:
            merged_intervals[-1][-1] = max(merged_intervals[-1][-1], i[-1])
        else:
            merged_intervals.append(i)
    return merged_intervals

def part1(data):
    intervals = []
    y = 2000000
    for sensor, closest_beacon in data:
        max_distance = manhattan(sensor, closest_beacon)
        distance_to_y = abs(y - sensor[1])
        if distance_to_y > max_distance:
            continue
        steps = max_distance - distance_to_y
        intervals.append([sensor[0] - steps, sensor[0] + steps])

    cannot_contain = sum([x2 - x1 + 1 for x1, x2 in merge_intervals(intervals)])
    sensors_on_y = sum([1 for sensor in set([sensor for sensor, _ in data]) if sensor[1] == y])
    beacons_on_y = sum([1 for beacon in set([beacon for _, beacon in data]) if beacon[1] == y])

    return cannot_contain - sensors_on_y - beacons_on_y
            

def part2(data):
    max_val = 4000000
    for y in range(max_val + 1):
        intervals = []
        for sensor, closest_beacon in data:
            max_distance = manhattan(sensor, closest_beacon)
            distance_to_y = abs(y - sensor[1])
            if distance_to_y > max_distance:
                continue
            steps = max_distance - distance_to_y
            interval = [max(0, sensor[0] - steps), min(max_val, sensor[0] + steps)]
            intervals.append(interval)

        intervals = merge_intervals(intervals)
        if len(intervals) == 2:
            return (intervals[0][1] + 1) * 4000000 + y


if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))