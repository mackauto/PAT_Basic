#! usr/bin/env python
#-*- coding: utf-8 -*-

num_str = input()

result = ""
if len(num_str) == 1:
    for num in range(int(num_str[0])):
        result += str(num+1)
elif len(num_str) == 2:
    result += "S" * int(num_str[0])
    for num in range(int(num_str[1])):
        result += str(num+1)
elif len(num_str) == 3:
    result += ("B" * int(num_str[0]) + "S" * int(num_str[1]))
    for num in range(int(num_str[2])):
        result += str(num+1)

print(result)