from pathlib import Path
import re
from collections import namedtuple
from queue import PriorityQueue, Queue
from typing import Set, List

State1 = namedtuple("State1", "pressure, v, t, opened, prev")
State2 = namedtuple("State2", "pressure, v1, v2, t1, t2, opened, prev")

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

def part1(data):
    flow_rates, dists = data

    start = State1(0, "AA", 30, set(), None)
    best = start
    visited_states = set()
    pq: PriorityQueue[State1] = PriorityQueue()
    pq.put(best)
    while not pq.empty():
        state = pq.get()
        best = state if state.pressure < best.pressure else best
        if (state.v, state.pressure, state.t) in visited_states:
            continue
        visited_states.add((state.v, state.pressure, state.t))


        new_states = [
            state._replace(
                pressure=state.pressure - (state.t - dist - 1) * flow_rates[valve],
                v=valve, 
                t=state.t - dist - 1, 
                opened={*state.opened, valve},
                prev=state
            )
            for valve, dist in dists[state.v].items() 
            if valve not in state.opened and dist <= state.t
        ]
        
        for new_state in new_states:
            pq.put(new_state)


    print_path(best)
    return -best.pressure

def print_path(state):
    if state.prev:
        print_path(state.prev)
    print(state._replace(pressure=-state.pressure, prev=None))

def part2(data):
    flow_rates, dists = data

    start = State2(0, "AA", "AA", 26, 26, set(), None)
    best = start
    visited_states = set()
    pq: PriorityQueue[State2] = PriorityQueue()
    pq.put(best)
    while not pq.empty():
        state = pq.get()
        best = state if state.pressure < best.pressure else best
        if (state.v1, state.v2, state.pressure, state.t1, state.t2) in visited_states:
            continue
        visited_states.add((state.v1, state.v2, state.pressure, state.t1, state.t2))

        
        new_states = [
            state._replace(
                pressure=state.pressure - (state.t1 - dist - 1) * flow_rates[valve],
                v1=valve, 
                t1=state.t1 - dist - 1, 
                opened={*state.opened, valve},
                prev=state
            )
            for valve, dist in dists[state.v1].items() 
            if valve not in state.opened and dist <= state.t1
        ] if state.t1 >= state.t2 else [
            state._replace(
                pressure=state.pressure - (state.t2 - dist - 1) * flow_rates[valve],
                v2=valve, 
                t2=state.t2 - dist - 1, 
                opened={*state.opened, valve},
                prev=state
            )
            for valve, dist in dists[state.v2].items() 
            if valve not in state.opened and dist <= state.t2
        ]

        for new_state in new_states:
            pq.put(new_state)

    print_path(best)
    return -best.pressure

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))