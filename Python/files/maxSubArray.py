class Solution:
	def maxSubArray(self, nums: [int]) -> int:
		if not nums:
			return 0

		localMaxima = float('-inf')
		globalMaxima = float('-inf')
		for num in nums:
			localMaxima = max(num, localMaxima+num)
			globalMaxima = max(globalMaxima, localMaxima)
		return globalMaxima
