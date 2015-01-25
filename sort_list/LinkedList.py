#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getLinkedListNode(n):
    count = 1
    node = ListNode(1)
    count += 1
    head = node
    while n != 1:
        node.next = ListNode(count)
        node = node.next
        count += 1
        n -= 1
    return head






# vim:ai:et:sts=4:sw=4:
