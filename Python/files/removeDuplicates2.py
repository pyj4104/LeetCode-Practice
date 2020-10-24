class Solution:
	def removeDuplicates(self, nums: [int]) -> int:
		curVal = -1
		length = 0
		counter = 0
		index = 0
		for num in nums:
			if num == curVal:
				if not counter == 2:
					nums[index] = curVal
					index += 1
					length += 1
					counter += 1
			if num != curVal:
				curVal = num
				nums[index] = curVal
				index += 1
				counter = 1
				length += 1

		return nums[:length]
