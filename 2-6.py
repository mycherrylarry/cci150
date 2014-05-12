#!/usr/bin/env python
from ListNode import ListNode, ListTestCase

head = ListTestCase(range(10)).head

p = head
while p.next!= None:
    p = p.next
p.next = head.next.next.next.next

p = head.next
q = head.next.next
while p != q:
    p = p.next
    q = q.next.next

head1 = q
lenA, lenB = 1, 1
p = head.next
while p != head1:
    lenA += 1
    p = p.next

p = head1.next
while p != head1:
    lenB += 1
    p = p.next
if cmp(lenA, lenB):
    pn = head
    pn1 = head1
else:
    pn = head1
    pn1 = head
for i in range(abs(lenA-lenB)):
    pn = pn.next
while pn != pn1:
    pn1 = pn1.next
    pn = pn.next
print pn.v
