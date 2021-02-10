from .basicClasses.Helper import Helper

class Solution:
	def largest1BorderedSquare(self, grid: [[int]]) -> int:
		seenOne = False
		for row in grid:
			for val in row:
				if val:
					seenOne = True
		if not seenOne:
			return 0

		distanceMat = [[(0,0)]] if grid[0][0] else [[None]]
		# Fill out the first row
		row = grid[0]

		for i, val in enumerate(row[1:]):
			x = distanceMat[0][i][0] + 1 if grid[0][i] else 0
			distance = (x, 0) if grid[0][i+1] else None
			distanceMat[0].append(distance)
		# Fill out the first col
		for i, row in enumerate(grid[1:]):
			y = distanceMat[i][0][1] + 1 if grid[i][0] else 0
			distance = (0, y) if grid[i+1][0] else None
			distanceMat.append([distance])

		for i, row in enumerate(grid[1:]):
			for j, val in enumerate(row[1:]):
				if not val:
					distance = None
				else:
					# i = y-axis, j = x-axis
					x = distanceMat[i+1][j][0] + 1 if distanceMat[i+1][j] else 0
					y = distanceMat[i][j+1][1] + 1 if distanceMat[i][j+1] else 0
					distance = (x, y)
				distanceMat[i+1].append(distance)

		maxArea = float('-inf')
		for i, row in enumerate(distanceMat):
			for j, val in enumerate(row):
				if val:
					x, y = val
					amountOfMaxSquare = min(x, y)
					if amountOfMaxSquare == 0:
						maxAreaForSquare = 1
					else:
						maxAreaForSquare = 1
						for k in range(1, amountOfMaxSquare+1):
							ny = i-k
							nx = j-k
							checkXVal = distanceMat[ny][j][0]
							checkYVal = distanceMat[i][nx][1]
							if checkXVal >= k and checkYVal >= k:
								maxAreaForSquare = (k+1)**2
					maxArea = max(maxAreaForSquare, maxArea)
		return maxArea

