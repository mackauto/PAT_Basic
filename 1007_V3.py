#! usr/bin/env python
#-*- coding: utf-8 -*-

# 该程序有一定的几率可以不超时通过最后一个测试点

import math

def is_prime(num):
    for div in range(2,int(math.sqrt(num))+1):
        if num % div == 0:
            return False
    return True

max_num = int(input())
count = 0

for num in range(5, max_num+1):
    if is_prime(num) and is_prime(num-2):
        count += 1

print(count)