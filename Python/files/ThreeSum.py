class Solution:
	def threeSum(self, nums: [int]) -> [[int]]:
		if len(nums) < 3:
			return []

		nums.sort()

		retVal = []
		oldVal = nums[0] - 1

		for i, num in enumerate(nums):
			b = i + 1
			c = len(nums) - 1
			if num != oldVal:
				while b < c:
					if num + nums[b] + nums[c] > 0:
						c -= 1
					elif num + nums[b] + nums[c] < 0:
						b += 1
					else:
						retVal.append([num, nums[b], nums[c]])
						bOldVal = nums[b]
						while bOldVal == nums[b] and b < c:
							b += 1
			oldVal = num

		return retVal
		
s = Solution()
testCases = [[-1, 0, 1, 2, -1, -4],
			[0, 0, 0, 0],
			[1, 2, -2, -1],
			[-2,0,0,2,2],
			[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]]
for case in testCases:
	print(s.threeSum(case))
