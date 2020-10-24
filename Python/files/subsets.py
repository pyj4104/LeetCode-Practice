class Solution:
	def subsets(self, nums: [int]) -> [[int]]:
		def dfs(nums: [int], path: [int], ans: [[int]]):
			ans.append(path)
			if nums:
				for i, num in enumerate(nums):
					dfs(nums[i+1:], path+[num], ans)
		ans = []
		dfs(nums, [], ans)

		return ans
