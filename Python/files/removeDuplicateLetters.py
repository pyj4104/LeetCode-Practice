class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
	    """
	    :type s: str
	    :rtype: str
	    """
	    if not s: return ""
	    counts = collections.Counter(list(s))
	    
	    pos = 0
	    for i, x in enumerate(s):
	        if x < s[pos]: pos = i
	        counts[x] -= 1
	        if counts[x] == 0: break

	    return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))
	