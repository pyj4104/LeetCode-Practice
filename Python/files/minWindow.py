class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        retVal = ""
        numChar, totCharLeft = self.processT(s, t)
        leftIndex, rightIndex = 0, 0
        while leftIndex < len(s):
            print(totCharLeft, leftIndex, rightIndex, len(s), numChar, s[leftIndex:rightIndex+1])
            if totCharLeft == 0:
                if not retVal:
                    retVal = s[leftIndex:rightIndex+1]
                else:
                    retVal = retVal if len(retVal) < len(s[leftIndex:rightIndex+1]) else s[leftIndex:rightIndex+1]
            if totCharLeft == 0 or (rightIndex == len(s)-1):
                leftIndex, totCharLeft = self.moveLeft(s, numChar, leftIndex, totCharLeft)
            else:
                rightIndex, totCharLeft = self.moveRight(s, numChar, rightIndex, totCharLeft)
        return retVal

    def moveLeft(self, s, numChar, lIndex, totCharLeft) -> (int, int):
        char = s[lIndex]
        if char in numChar:
            numChar[char][0] += 1
            if numChar[char][0] > 0:
                totCharLeft += 1
        lIndex += 1

        return lIndex, totCharLeft

    def moveRight(self, s, numChar, rIndex, totCharLeft) -> (int, int):
        rIndex += 1
        char = s[rIndex]
        if char in numChar:
            if numChar[char][0] > 0:
                totCharLeft -= 1
            numChar[char][0] -= 1
        return rIndex, totCharLeft
        
    def processT(self, s: str, t: str) -> ({}, int):
        numChar = {}
        totChar = 0
        for char in t:
            if char in numChar:
                numChar[char][0] += 1
                numChar[char][1] += 1
            else:
                numChar[char] = [1, 1]
            totChar += 1
        char = s[0]
        if char in numChar:
            numChar[char][0] -= 1
            totChar -= 1
        return numChar, totChar


# move left if totchar == 0 or left < right
# move right if totchar > 0 or right != len(s)-1
# break if 