from basicClasses.Helper import LinkedList, ListNode, TestSuites

class Solution:
	def removeDuplicates(self, nums: [int]) -> int:
		if not nums:
			return 0

		counter = 0
		lastItem = float('inf')

		for num in nums:
			if num != lastItem:
				nums[counter] = num
				lastItem = num
				counter += 1

		nums = nums[:counter]
		return len(nums)
		
s = Solution()
testCases = [[1, 2, 3, 4, 5], [1], [], [1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [1, 1]]
t = TestSuites(s, testCases, isLL = None, numArg = 1)
t.runTests('removeDuplicates')