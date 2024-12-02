def increase_or_decrease(arr):
    increase = sorted(arr)
    decrease = sorted(arr)[::-1]

    inc_dec = arr == increase or arr == decrease

    return inc_dec


def least_one_most_three(arr):
    p1 = 0
    p2 = 1
    ok = True
    for i in range(len(arr)-1):
        if not 1 <= abs(arr[p1] - arr[p2]) <= 3:
            ok = False
            break
        p1 += 1
        p2 += 1

    return ok


_input = \
    list(map(lambda x: list(map(int, x.split())), open('input_2.txt', 'r').readlines()))

som = 0
for i in _input:
    if not (increase_or_decrease(i) and least_one_most_three(i)):
        ok = False
        for k in range(len(i)):
            new_list = i[:k] + i[k+1:]
            if (increase_or_decrease(new_list) and
                    least_one_most_three(new_list)):
                ok = True

        if not ok:
            continue
    som += 1

print(som)
