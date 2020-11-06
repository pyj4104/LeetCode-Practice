class Solution:
	def spiralOrder(self, matrix: [[int]]) -> [int]:
		retVal = []
		dirs = ['r', 'd', 'l', 'u']
		direction = 0
		exitCounter = 0

		x,y = -1,0

		while True:
			nx, ny = self.calcNewCoordinates(x, y, direction)
			if self.availableToMove(nx, ny, matrix):
				retVal.append(matrix[ny][nx])
				x,y = nx, ny
				exitCounter = 0
				matrix[y][x] = float('-inf')
			else:
				direction = (direction + 1)%4
				exitCounter += 1
			if exitCounter == 2:
				break
		return retVal

	def availableToMove(self, x, y, matrix: [[int]]) -> bool:
		return True if y < len(matrix) and x < len(matrix[0]) and matrix[y][x] != float('-inf') else False

	def calcNewCoordinates(self, x: int, y: int, direction: int) -> (int,int):
		if direction == 0:
			x += 1
		elif direction == 1:
			y += 1
		elif direction == 2:
			x -= 1
		else:
			y -= 1
		return x,y
		