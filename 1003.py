#! usr/bin/env python
#-*- coding: utf-8 -*-

# 读入待检测的字符串的数量
count = int(input())

# 读入需要检测的字符串
string_list = []
while count != 0:
    string = input()
    string_list.append(string)
    count -= 1

# 检测字符串
for string in string_list:
    A_count = [0, 0, 0] # 记录字符串三个部分所含的A的数量
    pos = 0 # 位置指示变量，用来指示当前更新的是哪个部分
    flag = False # 指示变量，用来指示是否出现了P,A,T以外的字符
    for char in string:
        if char == 'A':
            A_count[pos] += 1
        elif char == 'P' and pos == 0:
            pos = 1
        elif char == 'T' and pos == 1:
            pos = 2
        else:
            flag = True
            break
    
    # 下面这个判断检验了文中所述的条件1，2，3，4
    if A_count[2] == A_count[0] * A_count[1] and A_count[1] and pos == 2 and not flag:
        print("YES")
    else:
        print("NO")