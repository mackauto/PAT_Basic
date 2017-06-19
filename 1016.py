#! usr/bin/env python
#-*- coding: utf-8 -*-

a, Da, b, Db = input().split()

count1 = a.count(Da)
count2 = b.count(Db)

def str_repeat(string, count):
     if count != 0:
         return string * count
     else:
         return "0"

a = str_repeat(Da, count1)
b = str_repeat(Db, count2)

print(int(a) + int(b))
