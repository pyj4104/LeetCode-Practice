class Solution:
	def minFallingPathSum(self, matrix: [[int]]) -> int:
		matLength = len(matrix)
		if matLength == 1:
			return min(matrix[0])
		for i in range(1, matLength):
			rowBefore = matrix[i-1]
			curRow = matrix[i]
			curRow[0] += min(rowBefore[0], rowBefore[1])
			for j in range(1, matLength-1):
				print('candidates:', rowBefore[j-1:j+2])
				curRow[j] += min(rowBefore[j-1:j+2])
			curRow[matLength-1] += min(rowBefore[matLength-1], rowBefore[matLength-2])
		return min(matrix[-1])
