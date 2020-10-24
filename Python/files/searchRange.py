class Solution:
	def searchRange(self, nums: [int], target: int) -> [int]:
		if not nums:
			return [-1, -1]

		if len(nums) == 1:
			if nums[0] == target:
				return [0,0]
			else:
				return [-1,-1]

		def condition(mid: int, retVal: [int], indexToRemember: int):
			if nums[mid] == target:
				retVal[indexToRemember] = mid

		retVal = [-1, -1]

		# find lower
		l, r = 0, len(nums)-1
		while l < r:
			mid = int((l+r)/2)

			condition(mid, retVal, 0)

			if nums[mid] < target:
				l = mid + 1
			else:
				r = mid

		# find upper
		l, r = 0, len(nums)-1
		while l < r:
			mid = int((l+r)/2)

			condition(mid, retVal, 1)

			if nums[mid] <= target:
				l = mid + 1
			else:
				r = mid

		condition(l, retVal, 1)

		if retVal[0] == -1:
			retVal[0] = retVal[1]

		return retVal
