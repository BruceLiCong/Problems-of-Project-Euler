#!/usr/bin/python

import math

def product(a, b):
    l = a
    s = b
    if a < b:
        l = b
        s = a
    i = s
    r = 1
    while i <= l:
        r = r * i
        i = i + 1
    return r

def problem15(n):
    i = 1
    t1 = product(n << 1, n + 1)
    t2 = product(n, 1)
    return t1 / t2

print problem15(1000)
