from math import sqrt

_inp = open('input_8.txt').read().strip()
_map = _inp.split('\n')


def get_all_antenas_coo(ant):
    coordinates = []
    for i in range(len(_map)):
        for j in range(len(_map[0])):
            if _map[i][j] == ant:
                coordinates.append((i, j))

    return coordinates


def calculate_antinodes(ant_local, coors):
    anti_nodes_coors = []
    for coor in coors:
        if coor == ant_local:
            anti_nodes_coors.append(coor)
            continue

        diff = (coor[0]-ant_local[0], coor[1]-ant_local[1])
        new_node = (coor[0]+diff[0], coor[1]+diff[1])
        line = new_node

        while True:
            if not (0 <= line[0] < len(_map) and 0 <= line[1] < len(_map[0])):
                break
            anti_nodes_coors.append(line)
            line = (line[0]+diff[0], line[1]+diff[1])
    print(anti_nodes_coors)

    return anti_nodes_coors


_antinodes_list = []


def nodes_in_map(antinodes):
    count = 0
    for antinode in antinodes:
        if (0 <= antinode[0] < len(_map) and 0 <= antinode[1] < len(_map[0])):
            if (antinode not in _antinodes_list):
                count += 1
                _antinodes_list.append(antinode)

    return count


answ = 0
for i in range(len(_map)):
    for j in range(len(_map[0])):
        if (_map[i][j] != '.' and _map[i][j] != '#' and _map[i][j] != '\n'):
            all_antenas = get_all_antenas_coo(_map[i][j])
            calc_antinodes = calculate_antinodes((i, j), all_antenas)
            answ += nodes_in_map(calc_antinodes)
print(answ)
