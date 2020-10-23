class Solution:
	def search(self, nums: [int], target: int) -> bool:
		headOnL = False
		mid = int((len(nums)-1)/2)
		l, r = 0, len(nums)-1

		if nums[mid] < nums[l]:
			r = mid
		else:
			l = mid

		while l < r:
			mid = int((l+r)/2)
			if nums[mid] <= nums[r]:
				r = mid
			else:
				l = mid + 1

		oriHead = l
		r = l - 1

		mid = int((oriHead + r)/2)
		