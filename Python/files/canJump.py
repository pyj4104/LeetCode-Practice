class Solution:
	def canJump(self, nums: [int]) -> bool:
		valVisited = [None] * len(nums)
		self.preCalc(nums, valVisited)
		#self.buildValVisited(nums, 0, valVisited)
		#self.buildValVisitedDPR(nums, valVisited)
		self.buildValVisitedGreedy(nums, valVisited)
		return valVisited[0]

	def preCalc(self, nums: [int], valVisited: [bool]):
		for i, num in enumerate(nums):
			if (i + num) >= len(nums)-1:
				valVisited[i] = True

	def buildValVisited(self, nums: [int], curPos: int, valVisited: [bool]) -> bool:
		if valVisited[curPos] is not None:
			return valVisited[curPos]

		valVisited[curPos] = False
		
		if curPos + nums[curPos] >= len(nums)-1:
			valVisited[curPos] = True
			return True
		
		for i in reversed(range(min(nums[curPos], len(nums)-1))):
			valVisited[curPos] = valVisited[curPos] or self.buildValVisited(nums, curPos+i+1, valVisited)
			if valVisited[curPos]:
				break

		return valVisited[curPos]

	def buildValVisitedDPR(self, nums: [int], valVisited: [bool]):
		for i in reversed(range(len(nums))):
			if not valVisited[i]:
				valVisited[i] = False or valVisited[i] if valVisited[i] is not None else False
				for j in range(min(nums[i], len(nums)-i-1)):
					if valVisited[i+j+1]:
						valVisited[i] = True

	def buildValVisitedGreedy(self, nums: [int], valVisited: [bool]):
		lastSmallestTrue = len(nums)-1
		for i in reversed(range(len(nums))):
			if nums[i]+i >= lastSmallestTrue:
				valVisited[i] = True
				lastSmallestTrue = i
			else:
				valVisited[i] = False
