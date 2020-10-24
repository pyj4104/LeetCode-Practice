class Solution:
	def generateMatrix(self, n: int) -> [[int]]:
		retVal = [[None]*n for i in range(n)]

		x,y = -1, 0
		direction = 0 #0 left, 1 down, 2 right, 3 up
		failedAttempts = 0
		val = 1

		while True:
			nx, ny = self.getNewCoordinate(x,y,direction)
			if self.checkAvailability(nx, ny, retVal, n):
				failedAttempts = 0
				retVal[ny][nx] = val
				val += 1
				x,y = nx,ny
			else:
				failedAttempts += 1
				direction = (direction+1)%4
			if failedAttempts == 2:
				break

		return retVal

	def printMatrix(self, matrix: [[int]]):
		for row in matrix:
			print(row)

	def checkAvailability(self, nx, ny, matrix, n) -> bool:
		if nx >= n or nx < 0:
			return False
		if ny >= n or ny < 0:
			return False
		if matrix[ny][nx]:
			return False
		return True

	def getNewCoordinate(self, x, y, direction) -> (int,int):
		nx, ny = x, y

		if direction == 0:
			nx += 1
		elif direction == 1:
			ny += 1
		elif direction == 2:
			nx -= 1
		else:
			ny -= 1

		return nx, ny
