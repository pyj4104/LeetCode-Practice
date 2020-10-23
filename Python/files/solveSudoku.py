class Solution:
	def solveSudoku(self, board: [[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		self.original = set()
		for i in range(9):
			self.original.add(str(i+1))

		possibles = self.constructPossibilities(board)
		rowPossible = possibles[0]
		columnPossible = possibles[1]
		sectorPossible = possibles[2]

		for y in range(9):
			for x in range(9):
				if board[y][x] == ".":
					allowed = rowPossible[y]&columnPossible[x]&sectorPossible[int(y/3)][int(x/3)]
					if len(allowed) == 1:
						num = list(allowed)[0]
						board[y][x] = list(allowed)[0]
						rowPossible[y].remove(num)
						columnPossible[x].remove(num)
						sectorPossible[int(y/3)][int(x/3)].remove(num)
		self.solve(board, rowPossible, columnPossible, sectorPossible)

	def getCoordinate(self, board: [[str]]) -> (int, int):
		for y in range(9):
			for x in range(9):
				if board[y][x] == ".":
					return x, y
		return -1, -1

	def solve(self, board: [[str]], rowPossible, columnPossible, sectorPossible) -> bool:
		x, y = self.getCoordinate(board)

		if x == -1:
			return True

		allowed = rowPossible[y]&columnPossible[x]&sectorPossible[int(y/3)][int(x/3)]

		if not len(allowed):
			return False

		for num in list(allowed):
			board[y][x] = num
			rowPossible[y].remove(num)
			columnPossible[x].remove(num)
			sectorPossible[int(y/3)][int(x/3)].remove(num)
			tryThis = self.solve(board, rowPossible, columnPossible, sectorPossible)
			if not tryThis:
				board[y][x] = "."
				rowPossible[y].add(num)
				columnPossible[x].add(num)
				sectorPossible[int(y/3)][int(x/3)].add(num)
			else:
				return True

		return False

	def constructPossibilities(self, board) -> []:
		original = self.original

		xPossible = []
		yPossible = []
		sectorPossible = []

		for y in range(9):
			row = self.original.copy()
			column = self.original.copy()
			for x in range(9):
				if board[y][x] in row:
					row.remove(board[y][x])
				if board[x][y] in column:
					column.remove(board[x][y])
			xPossible.append(row)
			yPossible.append(column)

		for i in range(3):
			row = []
			for j in range(3):
				startingY = i*3
				startingX = j*3
				sector = self.original.copy()
				for y in range(3):
					for x in range(3):
						if board[startingY+y][startingX+x] in sector:
							sector.remove(board[startingY+y][startingX+x])
				row.append(sector)
			sectorPossible.append(row)
		return [xPossible, yPossible, sectorPossible]
		