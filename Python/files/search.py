class Solution:
	def search(self, nums: [int], target: int) -> int:
		if len(nums) == 0:
			return -1
		elif len(nums) == 1:
			if nums[0] == target:
				return 0
			else:
				return -1

		# Find the min
		l = 0
		r = len(nums)-1
		pivotOnLeft = False

		while l < r:
			mid = int((l+r)/2)
			if nums[mid] > nums[r]:
				l = mid+1
			else:
				r = mid
		head = l

		l = 0
		r = len(nums)-1
		shiftBy = head

		trans = lambda x: (x+shiftBy)%len(nums)

		while l <= r:
			mid = int((l+r)/2)
			realMid = trans(mid)
			if nums[realMid] == target:
				return realMid
			elif nums[realMid] > target:
				r = mid-1
			else:
				l = mid+1

		return -1
		