from .basicClasses.Helper import Helper

class Solution:
	def minPathSum(self, grid: [[int]]) -> int:
		if len(grid[0]) == 0 or len(grid) == 0:
			return 0

		for x in range(1, len(grid[0])):
			grid[0][x] = grid[0][x-1] + grid[0][x]

		for y in range(1, len(grid)):
			grid[y][0] = grid[y-1][0] + grid[y][0]

		for y in range(1, len(grid)):
			for x in range(1, len(grid[0])):
				grid[y][x] += min(grid[y][x-1], grid[y-1][x])
		
		return grid[-1][-1]
