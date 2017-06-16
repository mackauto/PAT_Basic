#! usr/bin/env python
#-*- coding: utf-8 -*-

# 该程序在最后一个测试点运行超时

import math

max_num = int(input())
count = 0

prime_list = [2, 3]
for num in range(4, max_num+1):
    is_prime = True
    for div in prime_list:
        if div <= math.sqrt(num) + 1:
            if num % div == 0:
                is_prime = False
                break
        else:
            break

    if is_prime:
        if num - prime_list[-1] == 2:
            count += 1
        prime_list.append(num)

print(count)