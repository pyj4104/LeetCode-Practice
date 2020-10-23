class Solution:
	def permuteUnique(self, nums: [int]) -> [[int]]:
		retVal = []
		def dfs(nums, retVal, path, alreadyDiscovered):
			if len(nums) < 1:
				if str(path) not in alreadyDiscovered:
					retVal.append(path)
					alreadyDiscovered.add(str(path))
			else:
				for i, num in enumerate(nums):
					dfs(nums[:i]+nums[i+1:], retVal, path+[num], alreadyDiscovered)
		dfs(nums, retVal, [], set())
		return retVal
		