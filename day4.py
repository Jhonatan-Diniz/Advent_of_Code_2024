_inp = open('input_4.txt', 'r').read()

line_leng = len(_inp[:_inp.find('\n')])+1
current_line = 0

# part1

cont = 0
for i in range(len(_inp)):
    if (i % line_leng == 0):
        current_line += 1

    if (_inp[i:i+4] == 'XMAS' or _inp[i:i+4] == 'SAMX'):
        cont += 1

    if (current_line > _inp.count('\n')-3):
        continue

    col = _inp[i]+_inp[i+line_leng]+_inp[i+2*line_leng]+_inp[i+3*line_leng]

    if (col == 'XMAS' or col == 'SAMX'):
        cont += 1

    if (i % line_leng > line_leng - 5):
        continue

    diag1 = _inp[i]+_inp[i+line_leng+1]+_inp[i+2*line_leng+2]+_inp[i+3*line_leng+3]
    diag2 = _inp[i+3]+_inp[i+line_leng+2]+_inp[i+2*line_leng+1]+_inp[i+3*line_leng]

    if (diag1 == 'XMAS' or diag1 == 'SAMX'):
        cont += 1
    if (diag2 == 'XMAS' or diag2 == 'SAMX'):
        cont += 1

# print(cont)

# part2

cont = 0
current_line = 0
for i in range(len(_inp)):
    if (i % line_leng == 0):
        current_line += 1

    if (current_line > _inp.count('\n')-2):
        continue

    if (i % line_leng > line_leng - 3):
        continue

    diag1 = _inp[i] + _inp[i+line_leng+1] + _inp[i+2*line_leng+2]
    diag2 = _inp[i+2] + _inp[i+line_leng+1] + _inp[i+2*line_leng]

    if (diag1 == 'MAS' or diag1 == 'SAM') and (diag2 == 'MAS' or diag2 == 'SAM'):
        cont += 1
print(cont)
