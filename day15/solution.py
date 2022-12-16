from pathlib import Path
import re


def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    def manhattan(p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])
    with open(get_path(), "r") as file:
        data = [
            (sensor, beacon, manhattan(sensor, beacon))
            for sensor, beacon in [
                ((int(matches[0]), int(matches[1])), (int(matches[2]), int(matches[3])))
                for matches in (
                    re.findall("-?\d+", line)
                    for line in file.read().split("\n")
                )
            ]
        ]
    return data

def part1(data):
    intervals = []
    y = 2000000
    for sensor, _, manhattan in data:
        distance_to_y = abs(y - sensor[1])
        if distance_to_y > manhattan:
            continue
        steps = manhattan - distance_to_y
        intervals.append([sensor[0] - steps, sensor[0] + steps])
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = [sorted_intervals[0]]
    for i in sorted_intervals[1:]:
        if merged_intervals[-1][0] <= i[0] <= merged_intervals[-1][-1]:
            merged_intervals[-1][-1] = max(merged_intervals[-1][-1], i[-1])
        else:
            merged_intervals.append(i)

    cannot_contain = sum([x2 - x1 + 1 for x1, x2 in merged_intervals])
    sensors_on_y = sum([1 for sensor in set([sensor for sensor, _, _ in data]) if sensor[1] == y])
    beacons_on_y = sum([1 for beacon in set([beacon for _, beacon, _ in data]) if beacon[1] == y])
    return cannot_contain - sensors_on_y - beacons_on_y
            

def part2(data):
    def xy_to_pq(x, y): return x-y, x+y
    def pq_to_xy(p, q): return (p+q)//2, (q-p)//2
    pq = [
        xy_to_pq(u, v)
        for (x, y), _, d in data
        for u, v in ((x, y+d), (x-d, y), (x+d, y), (x, y-d))
    ]
    pp = sorted(set(p for p,_ in pq))
    qq = sorted(set(q for _,q in pq))
    p = [a+1 for a,b in zip(pp,pp[1:]) if b-a==2][0]
    q = [a+1 for a,b in zip(qq,qq[1:]) if b-a==2][0]
    x, y = pq_to_xy(p, q)
    return x*4_000_000 + y

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))