list_input = ''
with open('input_1.txt', 'r') as _input:
    list_input = \
        _input.read().replace('\n', ' ').replace('   ', ' ').split(' ')

left_list = []
right_list = []

for i in range(len(list_input)):
    if (list_input[i] == ''):
        continue
    if (i % 2 == 0):
        left_list.append(int(list_input[i]))
        continue
    right_list.append(int(list_input[i]))

left_list.sort()
right_list.sort()

part_1_answer = 0
for i in range(len(left_list)):
    part_1_answer += abs(right_list[i] - left_list[i])

part_2_answer = 0
for i in left_list:
    part_2_answer += right_list.count(i) * i

print("Part1 - ", part_1_answer)
print("Part2 - ", part_2_answer)
