class Solution:
	def searchInsert(self, nums: [int], target: int) -> int:
		return self.BruteForce(nums, target) == self.bSearch(nums, target)

	def bSearch(self, nums: [int], target: int) -> int:
		if not nums:
			return 0

		low = 0
		high = len(nums) - 1
		mid = 0

		while low <= high:
			mid = int(low + (high-low)/2)

			if nums[mid] == target:
				break

			if nums[mid] > target:
				high = mid-1
			elif nums[mid] < target:
				low = mid+1

		return low

	def BruteForce(self, nums: [int], target: int) -> int:
		if not nums:
			return 0

		small = float('-inf')
		large = nums[0]

		for i in range(0, len(nums)):
			large = nums[i]
			if target == large:
				return i
			elif target > small and target < large:
				return i
			small = nums[i]

		return len(nums)