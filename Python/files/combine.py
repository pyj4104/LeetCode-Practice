class Solution:
	def combine(self, n: int, k: int) -> [[int]]:
		nums = [i+1 for i in range(n)]
		ans = []

		def dfs(nums: [int], k: int, path: [int], ans: [[int]]):
			if len(path) == k:
				ans.append(path)
			else:
				for i, num in enumerate(nums):
					dfs(nums[i+1:], k, path+[num], ans)

		dfs(nums, k, [], ans)
		return ans

