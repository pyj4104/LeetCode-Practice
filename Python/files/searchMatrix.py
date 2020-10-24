class Solution:
	def searchMatrix(self, matrix: [[int]], target: int) -> bool:
		if not matrix or not matrix[0]:
			return False

		# Search Y Coordinate
		l, r = 0, len(matrix)-1
		while l <= r:
			mid = int((l+r)/2)
			if matrix[mid][0] <= target:
				l = mid + 1
			else:
				r = mid - 1
		column = r

		l, r = 0, len(matrix[0])-1

		print(target)

		while l <= r:
			mid = int((l+r)/2)
			if matrix[column][mid] == target:
				return True
			elif matrix[column][mid] < target:
				l = mid + 1
			else:
				r = mid - 1

		if matrix[column][r] == target:
			return True
		else:
			return False