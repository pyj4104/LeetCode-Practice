class Solution:
	def findMissingNumber(self, nums: [int]):
		if not nums:
			return 1

		l, r = 0, len(nums) - 1

		while l < r:
			mid = int((l+r)/2)

			if (nums[mid] - 1) != mid:
				r = mid
			else:
				l = mid + 1

		return l+1
		