#/usr/bin/python

def problem20(n):
    s = 1
    i = 1
    while i <= n:
        s = s * i
        i = i + 1

    l = str(s)
    t = 0
    
    for c in l:
        t = t + int(c)
    return t


print problem20(100)
