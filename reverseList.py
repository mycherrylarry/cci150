#!/usr/bin/env python
from ListNode import ListNode, ListTestCase

head = ListTestCase(range(10)).head

ListTestCase.prettyPrint(head)

def reverse(head):
    pre = None
    p = head.next
    while p != None:
        tmp = p.next
        p.next = pre
        pre = p
        p = tmp
    head.next = pre
    return head

ListTestCase.prettyPrint(reverse(head))

