#! usr/bin/env python
#-*- coding: utf-8 -*-

def gen_set(num):
    result_set = set()
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3*num + 1) / 2
        
        if num != 1:
            result_set.add(int(num))

    return result_set

total = int(input())
num_set = set(map(int, input().split()))

checked_set = set()
for element in num_set:
    if element not in checked_set:
        checked_set = checked_set | gen_set(element)
    else:
        continue

key_set = num_set - checked_set

key_list = sorted(key_set, reverse=True)

for ele in key_list:
    if ele != key_list[-1]:
        print(ele, end=' ')
    else:
        print(ele, end='')