class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        charList = {'-': -1, '+': 1}
        numList = {}
        for i in range(10):
            numList[str(i)] = i
        
        retVal = 0
        multiplier = 1
        pre = True
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] in charList:
            multiplier = charList[s[i]]
            i += 1

        while i < len(s):
            if s[i] in numList:
                retVal = retVal * 10 + numList[s[i]]
                i += 1
            else:
                break

        retVal = retVal * multiplier

        if multiplier == 1:
            retVal = min(retVal, (2**31)-1)
        else:
            retVal = max(retVal, (-2**31))
        return retVal

s = Solution()
'''print(s.myAtoi("words and 987"))
print(s.myAtoi("42"))
print(s.myAtoi("42"))
print(s.myAtoi("-42 52"))
print(s.myAtoi(""))
print(s.myAtoi(" "))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi(".1"))
print(s.myAtoi("-.1"))'''
s.myAtoi("-2147483649")
print(s.myAtoi("-2147483649"))
