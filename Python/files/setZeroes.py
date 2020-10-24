class Solution:
	def setZeroes(self, matrix: [[int]]) -> None:
		zeroesLoc = []
		for y in range(len(matrix)):
			for x in range(len(matrix[0])):
				if not matrix[y][x]:
					zeroesLoc.append((x,y))

		for zeroLoc in zeroesLoc:
			# turn xs to 0s first
			x = zeroLoc[0]
			for y in range(len(matrix)):
				matrix[y][x] = 0
			y = zeroLoc[1]
			for x in range(len(matrix[0])):
				matrix[y][x] = 0
