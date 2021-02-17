# input is between 2 and 58
class Solution:
	def integerBreak(self, n: int) -> int:
		if n == 2:
			return 1
		elif n == 3:
			return 2
		elif n == 4:
			return 4
		
		divisor = n // 3
		remaining = n % 3
		
		if remaining == 1:
			return 3**(divisor-1)*4
		elif remaining == 2:
			return 3**divisor*2
		else:
			return 3**divisor
