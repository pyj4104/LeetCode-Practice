class Solution:
	def rotate(self, matrix: [[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		newMatrix = self.rotateNaive(matrix)
		self.rotateOpti(matrix)
		print(newMatrix == matrix)


	def rotateNaive(self, matrix: [[int]]) -> [[int]]:
		newMatrix = []
		for height in range(len(matrix)):
			row = []
			for width in range(len(matrix)):
				row.append(0)
			newMatrix.append(row)
		for y in range(len(matrix)):
			for x in range(len(matrix[0])):
				newX, newY = self.getNewCoordinates(x, y, len(matrix[0])-1)
				newMatrix[newY][newX] = matrix[y][x]
		return newMatrix

	def rotateOpti(self, matrix: [[int]]) -> None:
		width = len(matrix[0])-1
		xTermination = len(matrix[0])-1
		rowIndex = 0
		trans = lambda x,y: (-y+width, x)
		while rowIndex < len(matrix)/2:
			xStarting = rowIndex
			while xStarting < xTermination:
				curX = xStarting
				curY = rowIndex
				newVal = matrix[curY][curX]
				for i in range(4):
					newX, newY = trans(curX, curY)
					temp = matrix[newY][newX]
					matrix[newY][newX] = newVal
					newVal = temp
					curX,curY=newX,newY
				xStarting += 1
			rowIndex += 1
			xTermination -= 1

	def getNewCoordinates(self, x:int, y:int, width: int) -> (int, int):
		newX, newY = -y+width, x
		return (newX,newY)

	def printMatrix(self, matrix: [[int]]):
		print('---')
		for row in matrix:
			print(row)
		print('---')