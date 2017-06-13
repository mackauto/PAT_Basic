#! usr/bin/env python
#-*-coding: utf-8 -*-

total = int(input())
num_list = list(map(int, input().split()))

num_list = sorted(num_list, reverse=True)

for index, num in enumerate(num_list, 1):
    if num == 1:
        count = 0
        break
    elif index < num:
        if index != total:
            continue
        else:
            count = total
    elif index >= num:
        count = index-1
        break

print(count)
