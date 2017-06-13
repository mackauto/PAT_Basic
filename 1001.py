#! usr/bin/env python
#-*- coding: utf-8 -*-

num = int(input())
count = 0

while num != 1:
    if num % 2 == 0:
        num = num / 2
    else:
        num = (num * 3 + 1) / 2

    count += 1

print(count)