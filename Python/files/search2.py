class Solution:
	def search(self, nums: [int], target: int) -> bool:
		for num in nums:
			if num == target:
				return True
		return False
