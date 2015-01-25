#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author:     ximing Zhao <ximing.zhao@108tian.com>
# Maintainer: ximing Zhao <ximing.zhao@108tian.com>

from LinkedList import getLinkedListNode

class Solution:
    def getLength(self, head):
        count = 1
        while head.next is not None:
            count += 1
            head = head.next
        return count

    def removeNthFromEnd(self, head, n):
        LinkLgth = self.getLength(head)

        # if n is 0 just return head
        if n == 0:
            return head
        # if is to del the first node, just return head.next
        if LinkLgth == n:
            return head.next

        NumToRemove = LinkLgth - n
        count = 1
        cursor = head
        while count != NumToRemove:
            cursor = cursor.next
            count += 1
        newCursor = cursor.next.next
        cursor.next = newCursor
        return head

    def printList(self, head):
        while head.next is not None:
            print head.val
            head = head.next
        # head.next is None but still it's a node should be print
        print head.val


if __name__ == "__main__":

    head = getLinkedListNode(10)
    s = Solution()
    s.printList(head)
    head = s.removeNthFromEnd(head, 3)
    s.printList(head)




# vim:ai:et:sts=4:sw=4:
