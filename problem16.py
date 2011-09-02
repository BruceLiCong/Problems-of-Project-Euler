#!/usr/bin/python

def problem16(n):
    a = 1
    i = 0
    s = 0
    while i < n:
        a = a << 1
        i = i + 1
    b = str(a)

    for c in b:
        s = s + int(c)
    return s

print problem16(1000)
