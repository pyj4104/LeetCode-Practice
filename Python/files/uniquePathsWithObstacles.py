from .basicClasses.Helper import Helper

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
		if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
			for i in range(len(obstacleGrid)):
				for j in range(len(obstacleGrid[0])):
					if obstacleGrid[i][j] == 1:
						return 0
			return 1

		for i in range(len(obstacleGrid)):
			for j in range(len(obstacleGrid[0])):
				obstacleGrid[i][j] -= 1

		xBlocked = False
		yBlocked = False

		if obstacleGrid[0][0] == 0:
			return 0

		for i in range(len(obstacleGrid)):
			if obstacleGrid[i][0] == -1 and not(yBlocked):
				obstacleGrid[i][0] = 1
			else:
				obstacleGrid[i][0] = 0
				yBlocked = True

		for j in range(1, len(obstacleGrid[0])):
			if obstacleGrid[0][j] == -1 and not(xBlocked):
				obstacleGrid[0][j] = 1
			else:
				obstacleGrid[0][j] = 0
				xBlocked = True

		Helper.PrintMatrix(obstacleGrid)

		for i in range(1, len(obstacleGrid)):
			for j in range(1, len(obstacleGrid[0])):
				obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) if obstacleGrid[i][j] == -1 else obstacleGrid[i][j]

		Helper.PrintMatrix(obstacleGrid)

		return max(obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1], 0)
