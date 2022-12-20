from pathlib import Path
import re
from queue import Queue

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def calc_dist(tunnels, from_valve, to_valve):
    bfs = Queue()
    visited = set()
    bfs.put((from_valve, 0))
    while bfs.qsize():
        valve, steps = bfs.get()
        if valve in visited:
            continue
        if valve == to_valve:
            return steps
        visited.add(valve)
        steps += 1
        for n_valve in tunnels[valve]:
            bfs.put((n_valve, steps))

def parse():
    with open(get_path(), "r") as file:
        data = {
            name: {
                "flow_rate": int(flow_rate), 
                "tunnels": tunnels
            } for name, flow_rate, *tunnels in (
                re.findall("[A-Z]{2}|\d+", line) 
                for line in file.read().split("\n")
            )
        }

    flow_rates = {k: v["flow_rate"] for k, v in data.items()}
    tunnels = {k: v["tunnels"] for k, v in data.items()}

    valves_with_flow = [k for k, v in flow_rates.items() if v]

    dists = {a: {b: 1000 for b in valves_with_flow} for a in (["AA"] + valves_with_flow) }

    for from_valve, valves_to_calc in dists.items():
        for to_valve in valves_to_calc.keys():
            dists[from_valve][to_valve] = calc_dist(tunnels, from_valve, to_valve)

    return flow_rates, dists

def all_orders(dists, valve, time, todo, path):
    for next_valve in todo:
        cost = dists[valve][next_valve] + 1
        if cost < time:
            yield from all_orders(dists, next_valve, time - cost, todo - {next_valve}, path + [next_valve])
    yield path
    
def calc_order(flow_rates, dists, start, order, time):
    pressure = 0
    cur = start
    for valve in order:
        time -= dists[cur][valve] + 1
        pressure += time * flow_rates[valve]
        cur = valve
    return pressure

def part1(data):
    flow_rates, dists = data
    orders = all_orders(dists, "AA", 30, {valve for valve, flow_rate in flow_rates.items() if flow_rate}, [])
    return max(calc_order(flow_rates, dists, "AA", order, 30) for order in orders)
    
def part2(data):
    flow_rates, dists = data
    orders = all_orders(dists, "AA", 26, {valve for valve, flow_rate in flow_rates.items() if flow_rate}, [])
    scores = [(calc_order(flow_rates, dists, "AA", order, 26), set(order)) for order in orders]
    scores.sort(key=lambda x: x[0], reverse=True)

    best = 0
    for i, (score1, order1) in enumerate(scores):
        if score1 * 2 < best:
            return best
        for score2, order2 in scores[i+1:]:
            if score1 + score2 < best:
                break
            if not order1 & order2:
                best = max(best, score1 + score2)

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))