class Solution:
	def isValidSudoku(self, board: [[str]]) -> bool:
		return (self.horizontalValidity(board) and\
			self.verticalValidity(board)) and\
			self.boxValidity(board)

	def horizontalValidity(self, board: [[str]]) -> bool:
		for i, row in enumerate(board):
			vals = set()
			for j, val in enumerate(row):
				if val != '.':
					if val in vals:
						return False
					else:
						vals.add(val)
		return True

	def verticalValidity(self, board: [[str]]) -> bool:
		i = 0
		while i < 9:
			j = 0
			vals = set()
			while j < 9:
				val = board[j][i]
				if val != '.':
					if val in vals:
						return False
					else:
						vals.add(val)
				j += 1
			i += 1

		return True

	def boxValidity(self, board: [[str]]) -> bool:
		xStartingPos = [0, 3, 6]
		yStartingPos = [0, 3, 6]
		for x in xStartingPos:
			for y in yStartingPos:
				vals = set()
				for i in range(3):
					for j in range(3):
						val = board[x+i][y+j]
						if val != '.':
							if val in vals:
								return False
							else:
								vals.add(val)
		return True