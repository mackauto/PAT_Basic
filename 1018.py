#! usr/bin/env python
#-*- coding: utf-8 -*-

# 该程序在其中一个测试点运行超时

total = int(input())

count = 1
list1 = [0, 0, 0]
list2 = [0, 0, 0]
dict1 = {
    'J' : 0,
    'C' : 0,
    'B' : 0,
}
dict2 = {
    'J' : 0,
    'C' : 0,
    'B' : 0,
}

while count <= total:
    one, two = input().split()
    if one == two:
        list1[1] += 1
        list2[1] += 1
    elif (one == 'J' and two == 'B') or (one == 'B' and two == 'C') or (one == 'C' and two == 'J'):
        list1[0] += 1
        list2[2] += 1
        dict1[one] += 1
    else:
        list1[2] += 1
        list2[0] += 1
        dict2[two] += 1

    count += 1

print(list1[0], list1[1], list1[2])
print(list2[0], list2[1], list2[2])

def find_max(dictionary):
    max_value = -1
    max_key = "Z"
    for k, v in dictionary.items():
        if v > max_value:
            max_value = v
            max_key = k
        elif v == max_value and k < max_key:
            max_key = k

    return max_key

print(find_max(dict1), find_max(dict2))