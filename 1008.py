#! usr/bin/env python
#-*- coding: utf-8 -*-

length, offset = map(int, input().split())
num_list = list(map(int, input().split()))

offset = offset % length

if offset == 0:
    new_list = num_list[:]
else:
    new_list = num_list[(offset * -1):] + num_list[:(length - offset)]

for index in range(0, len(new_list)):
    if index != len(new_list) - 1:
        print(new_list[index], end=' ')
    else:
        print(new_list[index], end='')