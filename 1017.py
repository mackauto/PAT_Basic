#! usr/bin/env python
#-*- coding: utf-8 -*-

a, n = list(map(int, input().split()))

r= a % n
div = (a - r) // n

print(div, r)