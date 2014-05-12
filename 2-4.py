#!/usr/bin/env python

from ListNode import ListNode, ListTestCase

head = ListTestCase(range(10)).head

def partition(head, value):
    pre = None
    post = pre
    p = head
    while p != None:
        if p.v <= value:
            #pre insert p
            temp_p = p
            temp_p.next = pre
            temp_pre = pre
            pre = temp_p
            pre.next = temp_pre.next
        else:
            #post insert p
            temp_p = p
            post.next = temp_p
            temp_p.next = None
            post = temp_p
        p = p.next





def insertFromHead(head):
    p = head
    q = None
    while p!= None:
        post = q
        tmp = p
        q = tmp
        p = p.next
        tmp.next = post

    return q

print [item for item in ListTestCase.list(insertFromHead(head))]
