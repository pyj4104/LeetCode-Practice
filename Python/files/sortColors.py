class Solution:
	def sortColors(self, nums: [int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		endOf0 = -1
		i = 0
		beginningOf2 = len(nums)
		while i < beginningOf2:
			if nums[i] == 0:
				nums.pop(i)
				nums.insert(0,0)
				endOf0 += 1
				i = max(endOf0, i - 1)
			elif nums[i] == 2:
				nums.pop(i)
				nums.append(2)
				beginningOf2 -= 1
				i = max(endOf0, i - 1)
			i += 1
