#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def getCompareNumber(self, num, highestDigitPosition):
        digitPosition = len(str(num))
        numStr = str(num)
        numList = [x for x in str(num)]
        tag = False
        while digitPosition < highestDigitPosition:
            tag = True
            numStr += numList[0]
            numList.append(numList.pop(0))
            digitPosition += 1
        fix = numStr[-len(str(num)):]
        fix = int(fix) - num
        if fix > 0:
            fix = float(fix)/(10 ** len(str(fix)))
        else:
            fix = float(fix)/(10 ** len(str(fix)) - 1)
        #print fix
        f = float(numStr)
        if tag:
            f += fix
        #print f
        return f

    def largestNumber(self,num):
        highestDigitPosition = max([len(str(x)) for x in num])
        num = sorted(num, key = lambda x: self.getCompareNumber(x,highestDigitPosition))
        num.reverse()
        returnStr =  "".join([str(x) for x in num])
        if returnStr.startswith("0"):
            returnStr = "0"
        return returnStr

if __name__ == "__main__":
    s = Solution()
    result = s.largestNumber([121,12])
    print result

# vim:ai:et:sts=4:sw=4:
