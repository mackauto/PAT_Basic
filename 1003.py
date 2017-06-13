#! usr/bin/env python
#-*- coding: utf-8 -*-

count = int(input())

string_list = []
while count != 0:
    string = input()
    string_list.append(string)
    count -= 1

for string in string_list:
    A_count = [0, 0, 0]
    pos = 0
    for char in string:
        if char == 'A':
            A_count[pos] += 1
        elif char == 'P' and pos == 0:
            pos = 1
        elif char == 'T' and pos == 1:
            pos = 2
        else:
            break

    if A_count[2] == A_count[0] * A_count[1] and A_count[1] and pos == 2:
        print("YES")
    else:
        print("NO")

