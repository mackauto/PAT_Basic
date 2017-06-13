#! usr/bin/env python
#-*- coding:utf-8 -*-

total = int(input())
count = 1

while count <= total:
    num_list = list(map(int, input().split()))
    if num_list[0] + num_list[1] > num_list[2]:
        print("Case #{}: true".format(count))
    else:
        print("Case #{}: false".format(count))

    count += 1