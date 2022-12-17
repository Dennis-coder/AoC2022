from pathlib import Path


def Shape1(y): 
    """
    ####
    """
    return set([
        (2,y), 
        (3,y), 
        (4,y), 
        (5,y)
    ])

def Shape2(y):
    """
    .#.
    ###
    .#.
    """
    return set([
        (3,y+2),
        (2,y+1),
        (3,y+1),
        (4,y+1),
        (3,y)
    ])

def Shape3(y):
    """
    ..#
    ..#
    ###
    """
    return set([
        (4,y+2),
        (4,y+1),
        (2,y),
        (3,y),
        (4,y)
    ])

def Shape4(y):
    """
    #
    #
    #
    #
    """
    return set([
        (2,y+3),
        (2,y+2),
        (2,y+1),
        (2,y),
    ])

def Shape5(y):
    """
    ##
    ##
    """
    return set([
        (2,y+1),
        (3,y+1),
        (2,y),
        (3,y)
   ] )

def move_left(shape):
    return set((x-1,y) for x,y in shape)

def move_right(shape):
    return set((x+1,y) for x,y in shape)

def move_down(shape):
    return set((x,y-1) for x,y in shape)

def is_valid_move(game, shape):
    for point in shape:
        if point in game: return False
        if point[0] == -1: return False
        if point[0] == 7: return False
        if point[1] == 0: return False
    return True

def get_path():
    cur_dir = Path().resolve().name
    if cur_dir == "AoC2022":
        return f"{Path(__file__).parent.name}/indata.txt"
    else:
        return "indata.txt"

def parse():
    with open(get_path(), "r") as file:
        data = [move_left if char == "<" else move_right for char in file.read().strip()]
    shape_switch = {
        0: Shape1,
        1: Shape2,
        2: Shape3,
        3: Shape4,
        4: Shape5,
    }
    return data, shape_switch

def part1(data):
    moves, shapes = data
    i_shape = 0
    i_jet = 0
    y = 0
    game = set()
    while i_shape < 2022:
        shape = shapes[i_shape%5](y+4)
        i_shape += 1
        while True:
            new_shape = moves[i_jet](shape)
            i_jet = (i_jet + 1) % len(moves)
            if is_valid_move(game, new_shape):
                shape = new_shape
            
            new_shape = move_down(shape)
            if is_valid_move(game, new_shape):
                shape = new_shape
            else:
                break
        for point in shape:
            game.add(point)
            y = max(y, point[1])
    
    return y

def part2(data):
    moves, shapes = data
    i_shape = 0
    i_moves = 0
    y = 0
    game = set()

    cycles = {}
    cycle = 0
    y_vals = {}

    while i_moves < len(moves) * 1.5:
        y_vals[i_shape] = y
        key = (i_shape % 5, i_moves % len(moves))
        if key in cycles:
            cycle = cycles[key], (i_shape, y)
        cycles[key] = (i_shape, y)
        shape = shapes[i_shape%5](y+4)
        i_shape += 1
        while True:
            new_shape = moves[i_moves % len(moves)](shape)
            i_moves += 1 
            if is_valid_move(game, new_shape):
                shape = new_shape
            
            new_shape = move_down(shape)
            if is_valid_move(game, new_shape):
                shape = new_shape
            else:
                break
        for point in shape:
            game.add(point)
            y = max(y, point[1])
    
    n = 1_000_000_000_000
    cycle_len = cycle[1][0] - cycle[0][0]
    cycle_val = cycle[1][1] - cycle[0][1]
    return n // cycle_len * cycle_val + y_vals[n % cycle_len]

if __name__ == "__main__":
    data = parse()
    print(part1(data))
    print(part2(data))