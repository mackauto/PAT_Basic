#! usr/bin/env python
#-*- coding: utf-8 -*-

# 定义映射关系
num_dict = {
    '0' : 'ling',
    '1' : 'yi',
    '2' : 'er',
    '3' : 'san',
    '4' : 'si',
    '5' : 'wu',
    '6' : 'liu',
    '7' : 'qi',
    '8' : 'ba',
    '9' : 'jiu',
}

# 读入
long_num_str = input()

# 遍历字符串，转换成整数，求和
sum_num = sum(list(map(int, long_num_str)))

# 按要求的格式打印结果
sum_str = str(sum_num)
for index in range(0, len(sum_str)):
    if index != len(sum_str) - 1:
        print(num_dict[sum_str[index]], end=' ')
    else:
        print(num_dict[sum_str[index]], end='')