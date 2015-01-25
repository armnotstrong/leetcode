#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author:     ximing Zhao <ximing.zhao@108tian.com>
# Maintainer: ximing Zhao <ximing.zhao@108tian.com>

class Solution:
    def __init__(self):
        self.stack = []

    def checkPaire(self, a,b):
        if a == "(" and b == ")":
            return True
        if a == "[" and b == "]":
            return True
        if a == "{" and b == "}":
            return True
        return False

    def isValid(self,s):
        #self.stack = [x for x in s]
        for x in s:
            if x == "[" or x == "(" or x == "{":
                self.stack.append(x)
            elif x == "]" or x == ")" or x == "}":
                try:
                    if not self.checkPaire(self.stack.pop(),x):
                        return False
                except:
                    return False
        if len(self.stack) != 0:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    print s.isValid("{}")


# vim:ai:et:sts=4:sw=4:
