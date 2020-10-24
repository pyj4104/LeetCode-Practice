class Solution:
	def qSort(self, nums: [int]) -> [int]:
		if len(nums) <= 1:
			return nums
		pivot = nums[0]
		lower = self.qSort([num for num in nums[1:] if num < pivot])
		higher = self.qSort([num for num in nums[1:] if num >= pivot])
		return lower+[pivot]+higher
	
	def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
		if not candidates:
			return []

		def dfs(candidates: [int], target: int, path: [int], sets: [int]):
			if target == 0:
				sets.append(path)
			elif target > 0:
				oldVal = float('-inf')
				for i, candidate in enumerate(candidates):
					if candidate != oldVal:
						dfs(candidates[i:i]+candidates[i+1:], target-candidate, path+[candidate], sets)
						oldVal = candidate

		candidates = self.qSort(candidates)
		retVal = []
		dfs(candidates, target, [], retVal)

		return retVal