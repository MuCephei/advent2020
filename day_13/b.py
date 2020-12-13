from functools import reduce

def parse_busses():
    with open('input.txt', 'r') as file:
        arrival = int(file.readline())
        for line in file.readlines():
            line = line.strip("\n")
            routes = line.split(",")
    return arrival, routes

def valid_time(id, offset, time):
    return (time + offset) % id == 0

def query(b, b_offset,start, period):
    t = start
    while True:
        if valid_time(b, b_offset, t):
            return t
        t += period


def win_contest(routes):
    named_routes = []
    start, period_list = 1, [1]
    for r in range(len(routes)):
        if routes[r] == 'x':
            continue
        id = int(routes[r])
        named_routes.append((id, r))
        period = reduce(lambda x, y:x*y, period_list)
        start = query(id, r, start, period)
        period_list.append(id)
    return start

_, routes = parse_busses()
print(win_contest(routes))