_inp = open('input_5.txt', 'r').read().strip()

rules = _inp.split('\n\n')[0]
content = _inp.split('\n\n')[1].split('\n')

rules1 = list(map(lambda x: int(x.split('|')[0]), rules.split('\n')))
rules2 = list(map(lambda x: int(x.split('|')[1]), rules.split('\n')))


def check(d):
    for y, k in enumerate(d):
        if k not in rules1:
            continue

        corresponds = [rules2[x] for x, y in enumerate(rules1) if y == k]
        intersection = list(set(corresponds) & set(d))

        if intersection == []:
            continue

        for i in intersection:
            if y > d.index(i):
                temp = d[y]
                d[y] = d.index(i)
                d[d.index(i)] = temp
    return d


for i in content:
    d = list(map(lambda x: int(x), i.split(',')))
    print(check(d))
