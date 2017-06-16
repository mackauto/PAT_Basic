#! usr/bin/env python
#-*- coding: utf-8 -*-

input_list = list(input().split())
output_list = input_list[::-1]

output_string = ""
for index in range(len(output_list)):
    if index != len(output_list) - 1:
        output_string += output_list[index] + ' '
    else:
        output_string += output_list[index]

print(output_string)