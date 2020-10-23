class Solution:
	def removeElement(self, nums: [int], val: int) -> int:
		if not nums:
			return 0
			
		index = 0

		for num in nums:
			if num != val:
				nums[index] = num
				index += 1

		return index