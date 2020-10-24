class Solution:
	def exist(self, board: [[str]], word: str) -> bool:
		def dfs(board: [[str]], word: str, searchLoc: (int, int)) -> bool:
			if not word:
				return True
			if not searchLoc:
				return False
			if word[0] == board[searchLoc[0]][searchLoc[1]]:
				board[searchLoc[0]][searchLoc[1]] = False
				newLocs = self.getNewLocs(board, searchLoc)
				for loc in newLocs:
					if dfs(board, word[1:], loc):
						return True
				board[searchLoc[0]][searchLoc[1]] = word[0]
			else:
				return False

		for i in range(len(board)):
			for j in range(len(board[0])):
				if dfs(board, word, (i,j)):
					return True

		return False

	def getNewLocs(self, board: [[str]], searchLoc: (int, int)) -> [(int,int)]:
		up = (searchLoc[0]-1, searchLoc[1]) if (searchLoc[0]-1) >= 0 else None
		down = (searchLoc[0]+1, searchLoc[1]) if (searchLoc[0]+1) < len(board) else None
		left = (searchLoc[0], searchLoc[1]-1) if (searchLoc[1]-1) >= 0 else None
		right = (searchLoc[0], searchLoc[1]+1) if (searchLoc[1]+1) < len(board[0]) else None
		searchLoc = [up, down, left, right]
		return [loc for loc in searchLoc]