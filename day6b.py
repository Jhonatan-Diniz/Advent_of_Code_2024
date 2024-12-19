_inp = open('input_6.txt').read()
_inp_lists = list(map(lambda x: list(x), _inp.split('\n')))


x, y = 0, 0

for i in range(len(_inp_lists)-1):
    for j in range(len(_inp_lists[0])-1):
        if (_inp_lists[i][j] == '^'):
            x, y = i, j


def checkLoops(obj, x, y):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    _dir = 0
    only_coordinates = set()

    while True:
        if ((x, y, _dir) in only_coordinates):
            return True

        only_coordinates.add((x, y, _dir))

        n_x = x + dirs[_dir][0]
        n_y = y + dirs[_dir][1]

        if not (0 <= n_x < len(_inp_lists)-1 and 0 <= n_y < len(_inp_lists)-1):
            break

        if (_inp_lists[n_x][n_y] == '#' or (n_x, n_y) == obj):
            _dir = (_dir + 1) % 4
            continue

        x = x + dirs[_dir][0]
        y = y + dirs[_dir][1]

    return False


cont = 0
for i in range(len(_inp_lists)-1):
    for j in range(len(_inp_lists[0])-1):
        checkloop = checkLoops((i, j), x, y)
        if checkloop:
            cont += 1

print(cont)
