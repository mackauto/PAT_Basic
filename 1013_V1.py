#! usr/bin/env python
#-*- coding: utf-8 -*-

# 该程序在其中一个测试点运行超时

import math

start, end = list(map(int, input().split()))

prime_list = [2, 3]
count = 2
num = 4

while count <= end:
    is_prime = True
    for div in prime_list:
        if div <= math.sqrt(num) + 1:
            if num % div == 0:
                is_prime = False
                break
        else:
            break

    if is_prime:
        count += 1
        prime_list.append(num)

    num += 1

pos = 1
for index in range(start-1, end):
    if pos % 10 != 0 and index != end-1:
        pos += 1
        print(prime_list[index], end=' ')
    elif pos % 10 == 0 and index != end-1:
        pos += 1
        print(prime_list[index], end='\n')
    elif index == end-1:
        print(prime_list[index], end='')