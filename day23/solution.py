def parse(file_name):
    with open(file_name, "r") as file:
        data = set([
            (x, y)
            for y, line in enumerate(file.read().splitlines())
            for x, char in enumerate(line)
            if char == "#"
        ])
    return data

def neighbours(x, y, round):
    positions = (
        (
            (x-1, y-1),
            (x, y-1),
            (x+1, y-1)
        ),
        (
            (x+1, y+1),
            (x, y+1),
            (x-1, y+1)
        ),
        (
            (x-1, y+1),
            (x-1, y),
            (x-1, y-1)
        ),
        (
            (x+1, y-1),
            (x+1, y),
            (x+1, y+1)
        )
    )
    return positions[round%4:] + positions[:round%4]

def simulate_round(elves, round):
    proposed_moves = {}
    proposed_moves_set = set()
    overlaping = set()
    for x, y in elves:
        possible_moves = []
        for a,b,c in neighbours(x, y, round):
            if a in elves or b in elves or c in elves:
                continue
            possible_moves.append(b)
        
        if len(possible_moves) % 4 == 0:
            proposed_moves[(x, y)] = (x, y)
            continue
        
        move = possible_moves[0]
        proposed_moves[(x, y)] = move
        if move in proposed_moves_set:
            overlaping.add(move)
        proposed_moves_set.add(move)
    return (
        {
            proposed_moves[elf] if proposed_moves[elf] not in overlaping else elf
            for elf in elves
        }, 
        bool(len(proposed_moves_set))
    )

def part1(elves):
    for round in range(10):
        elves, _ = simulate_round(elves, round)
    
    x_min = min(x for x,_ in elves)
    x_max = max(x for x,_ in elves)
    y_min = min(y for _,y in elves)
    y_max = max(y for _,y in elves)
    return  (x_max - x_min + 1) * (y_max - y_min + 1) - len(elves) 

def part2(elves):
    round = 0
    moved = True
    while moved:
        elves, moved = simulate_round(elves, round)
        round += 1
    return round
