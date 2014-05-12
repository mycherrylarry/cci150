#!/usr/bin/env python

def reverseString(s):
    return reduce(lambda x,y: x+y, list(s)[::-1])

print reverseString("abcd")
