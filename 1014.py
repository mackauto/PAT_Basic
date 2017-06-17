#! usr/bin/env python
#-*- coding: utf-8 -*-

import re

day_dict = {
    'A' : 'MON',
    'B' : 'TUE',
    'C' : 'WED',
    'D' : 'THU',
    'E' : 'FRI',
    'F' : 'SAT',
    'G' : 'SUN',
}

hour_dict = {
    '0' : '00',
    '1' : '01',
    '2' : '02',
    '3' : '03',
    '4' : '04',
    '5' : '05',
    '6' : '06',
    '7' : '07',
    '8' : '08',
    '9' : '09',
    'A' : '10',
    'B' : '11',
    'C' : '12',
    'D' : '13',
    'E' : '14',
    'F' : '15',
    'G' : '16',
    'H' : '17',
    'I' : '18',
    'J' : '19',
    'K' : '20',
    'L' : '21',
    'M' : '22',
    'N' : '23',
}

str1 = input()
str2 = input()
str3 = input()
str4 = input()

length1 = min([len(str1), len(str2)])
flag = False
for index in range(0, length1):
    if str1[index] == str2[index] and str1[index] in day_dict.keys() and not flag:
        day = day_dict[str1[index]]
        flag = True
        continue

    if str1[index] == str2[index] and str1[index] in hour_dict.keys() and flag:
        hour = hour_dict[str1[index]]
        break

length2 = min([len(str3), len(str4)])
for index in range(0, length2):
    if str3[index] == str4[index] and re.match('[a-z|A-Z]', str3[index]) != None:
        minus = index
        break

if minus < 10:
    print("{} {}:0{}".format(day, hour, minus))
else:
    print("{} {}:{}".format(day, hour, minus))