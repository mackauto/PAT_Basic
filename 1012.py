#! usr/bin/env python
#-*- coding: utf-8 -*-

import statistics

num_list = list(map(int, input().split()))

map_dict = {
    '0' : [],
    '1' : [],
    '2' : [],
    '3' : [],
    '4' : [],
}

for num in num_list[1:]:
    map_dict[str(num % 5)].append(num)

result_list = [0, 0 ,0, 0, 0]
for index in range(5):
    if index == 0:
        if map_dict[str(index)]:
            sum = 0
            for num in map_dict[str(index)]:
                if num % 2 == 0:
                    sum += num
            
            if sum != 0:
                result_list[index] = sum
            else:
                result_list[index] = "N"
        else:
            result_list[index] = "N"

    elif index == 1:
        if map_dict[str(index)]:
            sum = 0
            pre = 1
            for num in map_dict[str(index)]:
                sum += pre * num
                pre *= -1
            result_list[index] = sum
        else:
            result_list[index] = "N"

    elif index == 2:
        if map_dict[str(index)]:
            result_list[index] = len(map_dict[str(index)])
        else:
            result_list[index] = "N"

    elif index == 3:
        if map_dict[str(index)]:
            result_list[index] = format(statistics.mean(map_dict[str(index)]), '.1f')
        else:
            result_list[index] = "N"

    elif index == 4:
        if map_dict[str(index)]:
            result_list[index] = max(map_dict[str(index)])
        else:
            result_list[index] = "N"


for index in range(len(result_list)):
    if index != len(result_list) - 1:
        print(result_list[index], end=' ')
    else:
        print(result_list[index], end='')