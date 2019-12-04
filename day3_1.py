import math
def manhattan(point):
    return sum(map(abs, point))

def move(initial_loc, cmds):
    landed_loc = {}
    list_loc = []
    lat = initial_loc[0]
    lon = initial_loc[1]
    i = 0
    for cmd in cmds:
        direction, steps = cmd[0], int(cmd[1:])
        for _ in range(steps):
            i += 1
            if direction == 'U':
                lat += 1
            if direction == 'D':
                lat -= 1
            if direction == 'L':
                lon -= 1
            if direction == 'R':
                lon += 1
            landed_loc[(lat, lon)] = i 
    return landed_loc


def distance_measurement(loc):
    lat = loc[0]
    lon = loc[1]
    distance = abs(lat) + abs(lon)
    return distance


def main():
    with open('../input.txt') as f:
        data = f.read().split('\n')
    
    wire1, wire2 = data[0], data[1]
    
    wire1_cmds = wire1.split(',')
    wire2_cmds = wire2.split(',')
    
    loc_1, loc_2 = (0, 0), (0, 0)
    
    wire1_dict = move(loc_1, wire1_cmds)
    wire2_dict = move(loc_2, wire2_cmds)
    
    intersect_loc = set(wire1_dict) & set(wire2_dict)
    print(min([wire1_dict[loc] + wire2_dict[loc] 
            for loc in list(intersect_loc)]))



if __name__ == '__main__':
    main()