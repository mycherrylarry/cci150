#!/usr/bin/env python

def compress(s):
    ls = list(s)
    if len(ls) in (0, 1, 2): return s
    pre = ls[0]
    ns = []
    i = 1
    for item in ls[1:]:
        if pre == item:
            i += 1
        else:
            ns.append((pre, i))
            i = 1
            pre = item
    ns.append((pre, i))

    newS = ""
    for item in ns:
        a,b = item
        newS += (a+str(b))
    return len(newS) < len(s) and newS or s

print compress("abcccd")
print compress("ab")
print compress("abb")
print compress("aaabb")
print compress("aabcccccaaa")
            


