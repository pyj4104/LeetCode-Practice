class Solution:
	def numMovesToEqualizeBoxPiles(self, boxHeights: [int]) -> int:
		minHeight = float('inf')
		diffHeightPileSet = set()
		for height in boxHeights:
			minHeight = min(minHeight, height)
			if height not in diffHeightPileSet:
				diffHeightPileSet.add(height)
		boxHeights = sorted(boxHeights)[::-1]
		diffHeightPileList = sorted(diffHeightPileSet)[::-1]

		numMoves = 0
		diffHeightPileListIndex = 0
		boxHeightsIndex = 0
		while boxHeightsIndex < len(boxHeights):
			if boxHeights[boxHeightsIndex] == diffHeightPileList[diffHeightPileListIndex]:
				numMoves += len(diffHeightPileList) - diffHeightPileListIndex - 1
				boxHeightsIndex += 1
			else:
				diffHeightPileListIndex += 1
		return numMoves
