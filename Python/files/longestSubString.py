class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	charDict = {}
    	stIndex = 0
    	length = 1
    	retStIndex = stIndex
    	retLength = length

    	charDict[s[stIndex]] = 1

    	while (stIndex+length) < len(s):
    		edIndex = stIndex+length
    		if s[edIndex] in charDict:
    			del(charDict[s[stIndex]])
    			stIndex += 1
    			if length == 1:
    				charDict[s[stIndex]] = 1
    			else:
    				length -= 1
    		else:
    			charDict[s[edIndex]] = 1
    			length += 1
    			if length > retLength:
    				retStIndex = stIndex
    				retLength = length

    	return s[retStIndex: retStIndex + retLength]

sol = Solution()
print(sol.lengthOfLongestSubstring(s = "abcabcbb"))
print(sol.lengthOfLongestSubstring(s = "bbbbb"))
print(sol.lengthOfLongestSubstring(s = "pwwkew"))
print(sol.lengthOfLongestSubstring(s = "b"))

'''
pwwkew

charDict = {p, w}
stIndex = 0
length = 1
retStIndex = 0
retLength = 2
len(s) = 6

while :
	edIndex = 2
	s[edIndex] = w
'''