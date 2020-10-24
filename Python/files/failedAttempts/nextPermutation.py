from files.basicClasses.Helper import List, LinkedList, ListNode, TestSuites

class Solution:
	def quickSort(self, nums: [int]) -> [int]:
		if nums == []:
			return []

		x = nums[0]
		lower = self.quickSort([num for num in nums[1:] if num < x])
		upper = self.quickSort([num for num in nums[1:] if num >= x])

		return lower + [x] + upper

	def nextPermutation(self, nums: [int]) -> None:
		print(nums)
		"""
		Do not return anything, modify nums in-place instead.
		"""
		reverse = True
		before = nums[len(nums)-1]
		smallest = [-1, float("inf")]
		for i in range(len(nums)-1, -1, -1):
			if nums[i] < before:
				print(i, smallest)
				reverse = False
				nums[i], nums[smallest[0]] = smallest[1], nums[i]
				nums[i+1:] = self.quickSort(nums[i+1:])
				break
			if nums[i] < smallest[1]:
				smallest = [i, nums[i]]
			before = nums[i]

		if reverse:
			nums.reverse()

	def testTestSuites(self, listToChange: [int]) -> None:
		listToChange.append(5)
