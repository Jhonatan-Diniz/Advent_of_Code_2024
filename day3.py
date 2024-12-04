def mult(n1, n2):
    return n1*n2


_inp = open('input_3.txt', 'r').read()
do = True
answer = 0

for i in range(len(_inp)):
    if _inp[i:i+4] == 'do()':
        do = True
    if _inp[i:i+7] == "don't()":
        do = False
    if _inp[i:i+4] == 'mul(':
        mul_int = _inp[i+4:_inp.find(')', i+5)]
        ok = True
        if do:
            for char in mul_int:
                if (not char.isnumeric()) and char not in (',', ''):
                    ok = False
            if ok:
                answer += \
                    int(mul_int[:mul_int.find(',')]) * int(mul_int[mul_int.find(',')+1:])

print(answer)
