class Solution:
	def permute(self, nums: [int]) -> [[int]]:
		retVal = []
		def dfs(nums, retVal, path):
			if len(nums) < 1:
				retVal.append(path)
			else:
				for i, num in enumerate(nums):
					dfs(nums[:i]+nums[i+1:], retVal, path+[num])
		dfs(nums, retVal, [])
		return retVal
		