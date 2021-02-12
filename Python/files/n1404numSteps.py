class Solution:
	def numSteps(self, s: str) -> int:
		if len(s) == 1:
			return 0
		num = int(s, 2)
		ans = 0
		while num != 1:
			ans += 1
			if num%2 == 1:
				num += 1
			else:
				num //= 2
		return ans
		