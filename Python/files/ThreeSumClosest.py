class Solution:
	def qsort(self, inlist):
		if inlist == []: 
			return []
		else:
			pivot = inlist[0]
			lesser = self.qsort([x for x in inlist[1:] if x < pivot])
			greater = self.qsort([x for x in inlist[1:] if x >= pivot])
			return lesser + [pivot] + greater

	def threeSumClosest(self, nums: [int], target: int) -> int:
		if len(nums) < 3:
			return []

		diff = float("inf")
		nums = self.qsort(nums)

		retVal = 0

		for i, num in enumerate(nums):
			b = i + 1
			c = len(nums) - 1
			while b < c:
				val = num + nums[b] + nums[c]
				if abs(target-val) < diff:
					diff = abs(target-val)
					retVal = val
				if val-target > 0:
					c -= 1
				elif val-target < 0:
					b += 1
				else:
					return target

		return retVal
		
s = Solution()
testCases = [
			[[-1,2,1,-4], 1],
			[[0, 0, 0], 0],
			[[0, 2, 1, -3], 1],
			[[-3, 0, 1, 2], 1]
			]
for case in testCases:
	print(s.threeSumClosest(case[0], case[1]))
