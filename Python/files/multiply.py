class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		self.strToDigit = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
		n1 = self.str2Int(num1)
		n2 = self.str2Int(num2)
		return str(n1*n2)

	def str2Int(self, num: str) -> int:
		retVal = 0
		for digit in num:
			retVal = retVal * 10 + self.strToDigit[digit]
		return retVal