#!/usr/bin/env python

def replaceWhiteSpace(s):
    return reduce(lambda x,y: x+y, map(lambda x: "%20" if x == " " else x, list(s)))

print replaceWhiteSpace("abcde bb")
print replaceWhiteSpace("abcde bb   fasdf")
    

