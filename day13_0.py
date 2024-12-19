_inp = open('input_13.txt').read().split('\n\n')

tokens = 0

for a in _inp:
    ccc = 10**13
    i = a.split('\n')
    # The Prize position
    target = (int(i[2][i[2].find('X')+2:i[2].find(',')])+ccc,
              int(i[2][i[2].find('Y')+2:])+ccc)
    # Button A
    bA = (int(i[0][i[0].find('X')+2:i[0].find(',')]),

          int(i[0][i[0].find('Y')+2:]))
    # Button B
    bB = (int(i[1][i[1].find('X')+2:i[1].find(',')]),

          int(i[1][i[1].find('Y')+2:]))

    det = (bA[0]*bB[1] - bA[1]*bB[0])
    dX = (target[0]*bB[1]-target[1]*bB[0])
    dY = (target[0]*bA[1]-target[1]*bA[0])

    pushsA = dX/det
    pushsB = dY/det

    if not (pushsA % 1 == pushsB % 1 == 0):
        continue
    tokens += (abs(pushsA*3)+abs(pushsB))

print(tokens)
