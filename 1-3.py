#!/usr/bin/env python

def genMap(s):
    mp = {}
    for item in list(s):
        if mp.has_key(item):
            mp[item] += 1
        else:
            mp[item] = 1
    return mp

def checkPermutation(s1, s2):
    mp1 = genMap(s1)
    mp2 = genMap(s2)
    for item in list(s1):
        if not mp2.has_key(item):
            return "NO"
        if mp1[item] != mp2[item]:
            return "NO"
    for item in list(s2):
        if not mp1.has_key(item):
            return "NO"
        if mp2[item] != mp1[item]:
            return "NO"
    return "YES"

print checkPermutation("abc", "cbd")
print checkPermutation("abc", "cba")
