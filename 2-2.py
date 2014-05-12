#!/usr/bin/env python

class ListNode:
    def __init__(self, v):
        self.v = v
        self.next = None

def findKth(head, k):
    if k < 0:
        return None
    p, q = head, head
    while k>= 0 and q!= None:
        q = q.next
        k -= 1
    if k > 0:
        return None
    while q!= None:
        q = q.next
        p = p.next
    return p


li = [6,4,4,2,1,1,7,10]
pre = ListNode(li[0])
head = pre
for item in li[1:]:
    tmp = ListNode(item)
    pre.next = tmp
    pre = tmp

print findKth(head, 0).v
print findKth(head, 1).v
print findKth(head, 2).v

