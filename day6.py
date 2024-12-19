_inp = open('input_6.txt').read()
_inp_lists = list(map(lambda x: list(x), _inp.split('\n')))


x, y = 0, 0

for i in range(len(_inp_lists)-1):
    for j in range(len(_inp_lists[0])-1):
        if (_inp_lists[i][j] == '^'):
            x, y = i, j

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_dir = 0

area = 0

only_coordinates = set()

while True:
    only_coordinates.add((x, y))
    n_x = x + dirs[_dir][0]
    n_y = y + dirs[_dir][1]
    print("n_x: ", n_x)
    print('n_y: ', n_y)

    if not (0 <= n_x < len(_inp_lists)-1 and 0 <= n_y < len(_inp_lists)-1):
        break

    if (_inp_lists[n_x][n_y] == '#'):
        _dir = (_dir + 1) % 4
        continue

    x = x + dirs[_dir][0]
    y = y + dirs[_dir][1]

print(len(only_coordinates))
