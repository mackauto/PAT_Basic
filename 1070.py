#! usr/bin/env python
#-*-coding: utf-8 -*-

import math
from functools import reduce

count = int(input())
num_list = input().split()
num_list = list(map(int, num_list))
num_list =sorted(num_list)

result = reduce(lambda x,y: (x+y)/2, num_list)

print(math.floor(result))


