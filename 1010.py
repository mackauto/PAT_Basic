#! usr/bin/env python
#-*- coding: utf-8 -*-

num_list = list(map(int, input().split()))

result_list = []
for index in range(0, len(num_list)-1, 2):
    if len(num_list) == 2:
        result_list = [0, 0]
        break
    else:
        if num_list[index] * num_list[index+1] != 0:
            result_list.append(num_list[index] * num_list[index+1])
            result_list.append(num_list[index+1] - 1)

for index in range(0, len(result_list)):
    if index != len(result_list) - 1:
        print(result_list[index], end=' ')
    else:
        print(result_list[index], end='')