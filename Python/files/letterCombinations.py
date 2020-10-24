class Solution:
	NUMTOALPHABETLIST = {
	'2': ['a', 'b', 'c'],
	'3': ['d', 'e', 'f'],
	'4': ['g', 'h', 'i'],
	'5': ['j', 'k', 'l'],
	'6': ['m', 'n', 'o'],
	'7': ['p', 'q', 'r', 's'],
	'8': ['t', 'u', 'v'],
	'9': ['w', 'x', 'y', 'z']}

	def letterCombinations(self, digits: str) -> [str]:
		if len(digits) < 1:
			return ''

		for digit in digits:
			if digit == "1":
				return ''

		retVal = []
		self.recursiveLetterCombinations(digits, '', retVal)

		return retVal

	def recursiveLetterCombinations(self, digits: str, currentStr: str, ans: [str]):
		if len(digits) < 1:
			return ''

		lastNum = False

		if len(digits) == 1:
			lastNum = True

		for letter in self.NUMTOALPHABETLIST[digits[0]]:
			currentStr = currentStr + letter
			if lastNum:
				ans.append(currentStr)
			else:
				self.recursiveLetterCombinations(digits[1:], currentStr, ans)
			currentStr = currentStr[:len(currentStr)-1]
 
s = Solution()
testCases = ['29', '', '23', '1']
for testCase in testCases:
	print(s.letterCombinations(testCase))

