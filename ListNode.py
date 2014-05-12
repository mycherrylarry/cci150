#!/usr/bin/env python

class ListNode:
    def __init__(self, v):
        self.v = v
        self.next = None

class ListTestCase:
    def __init__(self, li):
        self.li = li
        self.head = ListNode(-1000000)
        self.head.next = self.genList(li)

    def genList(self, li):
        pre = ListNode(li[0])
        head = pre
        for item in li[1:]:
            tmp = ListNode(item)
            pre.next = tmp
            pre = tmp
        return head

    @staticmethod
    def list(head):
        p = head.next
        while p!= None:
            yield p.v
            p = p.next

    @staticmethod
    def prettyPrint(head):
        print [item for item in ListTestCase.list(head)]


def prettyPrint(f, *args):
    def new_f(*args):
        li = f(*args)
        return [item for item in ListTestCase.list(li)]
    return new_f

if __name__ == "__main__":
    head = ListTestCase(range(10)).head
    print [item for item in ListTestCase.list(head)]
