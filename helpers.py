from time import perf_counter

def timer(fn):
    def inner_timer(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        stop = perf_counter()
        return result, stop - start
    
    return inner_timer

def time_str(time):
    switch = {
        0: "s",
        1: "ms",
        2: "us",
        3: "ns",

    }
    i = 0
    while time < 1:
        time *= 1000
        i += 1
    
    return f"{time:.3f}{switch[i]}"