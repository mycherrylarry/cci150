#!/usr/bin/env python

from ListNode import ListNode, ListTestCase, prettyPrint

headA = ListTestCase(range(10)).head
headB = ListTestCase(range(10)).head

def sumList(headA, headB):
    headC = ListNode(-10000)
    pa, pb= headA.next, headB.next
    remainder = 0
    pc = headC
    while pa != None and pb != None:
        tmp = ListNode((pa.v + pb.v + remainder)%10)
        remainder = (pa.v + pb.v +remainder)/10
        pc.next = tmp
        pc = tmp
        pa = pa.next
        pb = pb.next
    pn = None
    if pa == None:
        pn = pb
    else:
        pn = pa
    while pn != None:
        tmp = ListNode((pn.v + remainder)%10)
        remainder = (pn.v + remainder)/10
        pc.next = tmp
        pc = tmp
        pn = pn.next
    if remainder != 0:
        tmp = ListNode(remainder)
        pc.next = tmp
        pc = tmp
    return headC



#print [item for item in ListTestCase.list(sumList(headA, headB))]
print sumList(headA, headB)
print ListTestCase.prettyPrint(sumList(headA, headB))
print 9876543210*2
