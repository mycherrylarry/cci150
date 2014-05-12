#!/usr/bin/env python

def checkUnique(s):
    mp = {}
    for item in list(s):
        if mp.get(item) == 1:
            return "NO"
        mp[item] = 1
    return "YES"

def checkUnique1(s):
    return len(set(list(s))) == len(list(s)) and "YES" or "NO"


print checkUnique("hello")
print checkUnique("abcdefg")

print checkUnique1("hello")
print checkUnique1("abcdefg")
