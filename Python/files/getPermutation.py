class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		print(self.optSol(n,k))
		print(self.dfsSol(n,k))
		assert self.optSol(n,k) == self.dfsSol(n,k)
		return self.dfsSol(n,k)

	def dfsSol(self, n:int, k:int) -> str:
		sols = {}
		arrSpace = []
		for i in range(n):
			arrSpace.append(i+1)
		def dfs(arrSpace: [int], curPos: [int], curStr: str):
			if not arrSpace:
				sols[curPos[0]] = curStr
				curPos[0] += 1
			for i, num in enumerate(arrSpace):
				dfs(arrSpace[:i]+arrSpace[i+1:], curPos, curStr+str(num))
		dfs(arrSpace, [0], '')
		return sols[k-1]

	def optSol(self, n:int, k:int) -> str:
		itemsInQuad = 1
		nums = []
		for i in range(n-1):
			itemsInQuad *= (i+1)
			nums.append(i+1)
		nums.append(n)

		def searchDFS(nums: [int], k: int, path: str, itemsInQuad: int):
			if len(nums) == 1:
				return path+str(nums[0])
			quadrant = int(k/itemsInQuad)
			nextk = k%itemsInQuad
			return searchDFS(nums[:quadrant]+nums[quadrant+1:], nextk, path+str(nums[quadrant]), int(itemsInQuad/(len(nums)-1)))

		return searchDFS(nums, k-1, '', itemsInQuad)


