import heapq as h

class Solution:
	def eatenApples(self, apples: [int], days: [int]) -> int:
		pQueue = []
		dateToday = 0
		numEaten = 0
		for i in range(len(days)):
			h.heappush(pQueue, [days[dateToday]+dateToday, apples[dateToday]])
			foundStoredApple = False
			while pQueue and not foundStoredApple:
				thingsToEat = h.heappop(pQueue)
				if thingsToEat[0] > dateToday and thingsToEat[1] > 0:
					foundStoredApple = True
			if foundStoredApple:
				numEaten += 1
				thingsToEat[1] -= 1
			if thingsToEat[0] > dateToday and thingsToEat[1] > 0:
				h.heappush(pQueue, thingsToEat)
			dateToday += 1
		while pQueue:
			thingsToEat = h.heappop(pQueue)
			if thingsToEat[0] > dateToday and thingsToEat[1] > 0:
				numEaten += 1
				thingsToEat[1] -= 1
			else:
				continue
			h.heappush(pQueue, thingsToEat)
			dateToday += 1
		return numEaten
