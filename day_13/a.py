def parse_busses():
    with open('test_input.txt', 'r') as file:
        arrival = int(file.readline())
        for line in file.readlines():
            line = line.strip("\n")
            routes = line.split(",")
    return arrival, routes

def shortest_time(arrival, routes):
    current_min = None
    result = 0
    for route in routes:
        if route == 'x':
            continue
        id = int(route)
        time = arrival % id
        if time != 0:
            time = id - time
        if current_min is None or time < current_min:
            current_min = time
            result = time * id
    return result

arrival, routes = parse_busses()
print(shortest_time(arrival, routes))