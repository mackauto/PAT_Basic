#! usr/bin/env python
#-*-coding: utf-8 -*-

count = int(input())
name, number, score = input().split()

min_name = name
max_name = name

min_number = number
max_number = number

min_score = int(score)
max_score = int(score)

for index in range(count-1):
    temp_name, temp_number, temp_score = input().split()
    temp_score = int(temp_score)
    if temp_score > max_score:
        max_name = temp_name
        max_number = temp_number
        max_score = temp_score
    if temp_score < min_score:
        min_name = temp_name
        min_number = temp_number
        min_score = temp_score

print(max_name, max_number)
print(min_name, min_number)


