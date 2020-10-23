class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		if not s:
			return 0

		x = len(s) - 1
		while x >= 0 and s[x] == " ":
			x -= 1

		retVal = 0
		while x >= 0 and s[x] != " ":
			retVal += 1
			x -= 1

		return retVal