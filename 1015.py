#! usr/bin/env python
#-*- coding: utf-8 -*-

# 该程序在其中三个测试点运行超时

total, low, high = list(map(int, input().split()))

list1, list2, list3, list4, drop_list = [], [], [], [], []

count = 1
while count <= total:
    temp_list = []
    for element in list(map(int, input().split())):
        temp_list.append(element)
    temp_list.append(temp_list[1] + temp_list[2])

    if temp_list[1] >= high and temp_list[2] >= high:
        list1.append(temp_list)
    elif temp_list[1] < low or temp_list[2] < low:
        drop_list.append(temp_list)
    elif temp_list[1] >= high and temp_list[2] < high:
        list2.append(temp_list)
    elif  temp_list[1] <= high and temp_list[2] <= high and temp_list[1] >= temp_list[2]:
        list3.append(temp_list)
    else:
        list4.append(temp_list)

    count += 1

sort_func = lambda lst: (lst[3]*-1, lst[1]*-1, lst[0])

list1 = sorted(list1, key = sort_func)
list2 = sorted(list2, key = sort_func)
list3 = sorted(list3, key = sort_func)
list4 = sorted(list4, key = sort_func)
total_list = list1 + list2 + list3 + list4

print(total - len(drop_list))
for item in total_list:
    print("{} {} {}".format(item[0], item[1], item[2]))