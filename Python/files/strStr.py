class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if not needle:
			return 0
			
		needleLen = len(needle)

		for i, char in enumerate(haystack):
			if char == needle[0]:
				if haystack[i:i+needleLen] == needle:
					return i
		
		return -1