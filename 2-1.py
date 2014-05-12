#!/usr/bin/env python

class ListNode:
    def __init__(self, v):
        self.v = v
        self.next = None

def deleteDups(head):
    mp = {}
    mp[head.v] = head
    pre = head
    t = pre.next
    while t != None:
        if mp.has_key(t.v):
            pre.next = t.next
        else:
            mp[t.v] = t
        pre = t
        t = t.next
    return head

li = [6,4,4,2,1,1,7,10]
pre = ListNode(li[0])
head = pre
for item in li[1:]:
    tmp = ListNode(item)
    pre.next = tmp
    pre = tmp

head = deleteDups(head)

while head != None:
    print head.v
    head = head.next

