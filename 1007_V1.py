#! usr/bin/env python
#-*- coding: utf-8 -*-

# 该程序在最后一个测试点运行超时

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n != 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

max_num = int(input())
prime = primes()

present_prime = next(prime)
count = 0

while present_prime <= max_num:
    next_prime = next(prime)
    if next_prime - present_prime == 2 and next_prime <= max_num:
        count += 1
    
    present_prime = next_prime

print(count)
