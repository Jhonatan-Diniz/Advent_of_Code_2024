def increase_or_decrease(arr):
    return (sorted(arr) == arr or sorted(arr)[::-1] == arr)


def least_one_most_three(arr):
    for i in range(len(arr)-1):
        if not (1 <= abs(arr[i] - arr[i+1]) <= 3):
            return False
    return True


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
