class Solution:
	def climbStairs(self, n: int) -> int:
		ans = self.climbStairsDP(n)
		assert self.climbStairsDC(n) == ans
		return ans

	def climbStairsDP(self, n: int) -> int:
		memory = [-1]*(n+1)
		memory[0], memory[1] = 1, 1

		def helper(n: int, memory: [int]) -> int:
			if n < 0:
				return 0

			if memory[n] != -1:
				return memory[n]

			memory[n] = helper(n-2, memory) + helper(n-1, memory)

			return memory[n]

		return helper(n, memory)

	def climbStairsF(self, n: int) -> int:
		if n == 1:
			return 1

		first, second = 1,2
		for i in range(3, n+1):
			third = first + second
			first = second
			second = third
		return second

	def dynamic(self, n: int) -> int:
		if n == 1:
			return 1

		memory = [-1] * (n+1)
		memory[1], memory[2] = 1, 2

		for i in range(3, n+1):
			memory[i] = memory[i-1] + memory[i-2]

		return memory[n]


	def climbStairsDC(self, n: int) -> int:
		if n < 0:
			return 0

		if n == 0:
			return 1
			
		if n == 1:
			return 1

		return self.climbStairsDC(n-2) + self.climbStairsDC(n-1)
